import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

async function main () {
  await client.connect();
  await client.hSet('HolbertonSchools', {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  }, print);
  const values = await client.hGetAll('HolbertonSchools');
  console.log(Object.assign({}, values));
}

main();
