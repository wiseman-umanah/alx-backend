import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

async function publishMessage (message, time) {
  setInterval(() => {
    console.log('About to send', message);
    client.publish('holberton school channel', JSON.stringify(message));
  }, time);
}

async function main () {
  await client.connect();
  await publishMessage('Holberton Student #1 starts course', 100);
  await publishMessage('Holberton Student #2 starts course', 200);
  await publishMessage('KILL_SERVER', 300);
  await publishMessage('Holberton Student #3 starts course', 400);
}

main();
