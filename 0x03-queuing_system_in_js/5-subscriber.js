import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

async function main () {
  await client.connect();
  client.subscribe('holberton school channel', async (msg) => {
    if (msg === JSON.stringify('KILL_SERVER')) {
      console.log(msg);
      await client.unsubscribe('holberton school channel');
      await client.quit();
    }
    console.log(msg);
  });
}

main();
