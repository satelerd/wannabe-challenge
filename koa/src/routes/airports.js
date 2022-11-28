const Router = require('koa-router');

const router = new Router();

const airports = [
    {
        iata_code: 'ABE',
        airport: 'Lehigh Valley International Airport',
        city: 'Allentown',
        state: 'PA',
        country: 'USA',
        latitude: 40.652083,
        longitude: -75.440806,
    },
    {
        iata_code: 'ABI',
        airport: 'Abilene Regional Airport',
        city: 'Abilene',
        state: 'TX',
        country: 'USA',
        latitude: 32.411319,
        longitude: -99.681897,
    }
];

// GET /airports
router.get('airports.show', '/', (ctx) => {
    ctx.body = JSON.stringify(airports);
});

router.get('airports.show', '/:iata_code', (ctx) => {
    const airport = airports.find((airport) => {
        return airport.iata_code === ctx.params.iata_code;
    });

    if (airport) {
        ctx.body = JSON.stringify(airport);
    } else {
        ctx.status = 404;
    }
});

module.exports = router;