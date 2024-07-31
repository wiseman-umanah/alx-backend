import express from 'express';
import { createClient } from 'redis';

const client = createClient();
client.on('connect', () => console.log('Redis started'));

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
];

function getItemById (id) {
  return listProducts.find(data => data.id === id);
}

function reserveStockById (itemId, stock) {
  client.set(itemId.toString(), stock);
}

async function getCurrentReservedStockById (itemId) {
  const availableStock = await client.get(itemId.toString());
  return availableStock ? parseInt(availableStock) : 0;
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const data = getItemById(itemId);

  if (!data) {
    return res.json({ status: 'Product not found' });
  }

  try {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = data.stock - reservedStock;
    data.available_stock = availableStock;
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: 'Error retrieving reserved stock' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const data = getItemById(itemId);

  if (!data) {
    return res.json({ status: 'Product not found' });
  }

  try {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const temp = data.stock - reservedStock;
    if (temp > 0) {
      reserveStockById(itemId, reservedStock + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'Not enough stock available', itemId });
    }
  } catch (err) {
    res.status(500).json({ error: 'Error reserving stock' });
  }
});

async function main () {
  try {
    await client.connect();
  } catch (err) {
    console.log('Error Status: cannot connect to Redis, check connection');
  }
}

app.listen(port);
main();
