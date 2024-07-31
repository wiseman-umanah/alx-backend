import kue from 'kue';

const queue = kue.createQueue();
queue.setMaxListeners(30);

const blackList = ['4153518780', '4153518781'];

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

function sendNotification (phoneNumber, message, job, done) {
  let progress = 0;
  const stop = 100;

  const progressInterval = setInterval(() => {
    job.progress(progress, stop);
    progress += 50;

    if (blackList.includes(phoneNumber)) {
      clearInterval(progressInterval);
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    if (progress >= stop) {
      clearInterval(progressInterval);
      done();
    }

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }, 1000);
}

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Create jobs
jobs.forEach(data => {
  const job = queue.create('push_notification_code_2', data)
    .removeOnComplete(true)
    .save((err) => {
      if (err) {
        console.log('Notification job failed:', err);
      } else {
        console.log('Notification job created:', job.id);
      }
    });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log('Notification job failed:', err);
  }).on('progress', (progress) => {
    console.log(`Notification job #${job.id} ${progress}% complete`);
  });
});
