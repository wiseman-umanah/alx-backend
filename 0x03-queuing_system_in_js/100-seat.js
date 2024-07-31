import { createClient } from 'redis';
import kue from 'kue';
import express from 'express';

const client = createClient();
const queue = kue.createQueue();
const app = express();
const port = 1245;

let reservationEnabled = true;

async function main () {
  await client.connect();
  await reserveSeat(50);
  console.log('Redis connection established');
}

async function reserveSeat (number) {
  await client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const seatNum = await client.get('available_seats');
  return parseInt(seatNum, 10) || 0;
}

queue.process('reserve_seat', async (job, done) => {
  try {
    let num = await getCurrentAvailableSeats();
    num = num - 1;
    console.log(num);
    await reserveSeat(num);

    if (num === 0) {
      reservationEnabled = false;
    }

    if (num >= 0) {
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  } catch (err) {
    done(err);
  }
});

app.get('/available_seats', async (req, res) => {
  try {
    const num = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: num });
  } catch (err) {
    res.status(500).json({ error: 'Error retrieving available seats' });
  }
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled) {
    const job = queue.create('reserve_seat')
      .removeOnComplete(true)
      .save((err) => {
        if (err) {
          res.status(500).json({ status: 'Reservation failed', error: err.message });
        } else {
          res.json({ status: 'Reservation in process' });
        }
      });

    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
  } else {
    res.json({ status: 'Reservations are blocked' });
  }
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
});

main();

app.listen(port);
