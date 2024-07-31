import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', data)
  .save((err) => {
    if (err) {
      console.log('Notification job failed:', err);
    } else {
      console.log('Notification job created:', job.id);
    }
  });

function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

job.on('complete', () => {
  sendNotification(data.phoneNumber, data.message);
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed:', err);
});
