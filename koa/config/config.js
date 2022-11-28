const dotenv = require('dotenv');
dotenv.config();

module.exports = {
  "development": {
    "username": "wannabe",
    "password": 12345678,
    "database": "database_development",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "test": {
    "username": "wannabe",
    "password": 12345678,
    "database": "database_test",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "username": "wannabe",
    "password": 12345678,
    "database": "database_production",
    "host": "127.0.0.1",
    "dialect": "postgresql"
  }
}

// change the module.exports to use env variables

module.exports = {
  "development": {
    "username": process.env.DB_USER,
    "password": process.env.DB_PASSWORD,
    "database": `${process.env.DB_NAME}_development`,
    "host": process.env.DB_HOST,
    "dialect": "postgres"
  },
  "test": {
    "username": process.env.DB_USER,
    "password": process.env.DB_PASSWORD,
    "database": `${process.env.DB_NAME}_test`,
    "host": process.env.DB_HOST,
    "dialect": "postgres"
  },
  "production": {
    "username": process.env.DB_USER,
    "password": process.env.DB_PASSWORD,
    "database": `${process.env.DB_NAME}_production`,
    "host": process.env.DB_HOST,
    "dialect": "postgresql"
  }
}
