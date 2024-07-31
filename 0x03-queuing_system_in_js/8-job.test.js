import { describe, it, beforeEach, afterEach } from 'mocha';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import sinon from 'sinon';

describe('createPushNotificationsJobs', function () {
  let queue;
  let spy;

  beforeEach(function () {
    queue = kue.createQueue();
    spy = sinon.spy(queue, 'create');
  });

  afterEach(function () {
    spy.restore();
  });

  it('should create a job with valid data', function () {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);
    expect(spy.calledWith('push_notification_code_3', list[0])).to.be.true;
  });

  it('should throw an error if jobs is not an array', function () {
    const list = 'hello';
    expect(() => createPushNotificationsJobs(list, queue)).to.throw('Jobs is not an array');
  });

  it('should create multiple jobs with valid data', function () {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);
    expect(spy.calledTwice).to.be.true;
  });

  it('should set the correct job properties', function () {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);
  });
});
