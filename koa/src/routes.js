import Router from 'koa-router';
import airlines from './routes/airlines.js';
import airports from './routes/airports.js';
import flights from './routes/flights.js';

const router = new Router();

router.use('/airlines', airlines.routes());
router.use('/airports', airports.routes());
router.use('/flights', flights.routes());

export default router;