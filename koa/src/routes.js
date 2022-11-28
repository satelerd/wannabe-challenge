const Router = require('koa-router');
const airlines = require('./routes/airlines.js');
const airports = require('./routes/airports.js');
const flights = require('./routes/flights.js');


const router = new Router();

router.use('/airlines', airlines.routes());
router.use('/airports', airports.routes());
router.use('/flights', flights.routes());

module.exports = router;