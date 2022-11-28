const Router = require('koa-router');

const router = new Router();

const flights = [
    {
        id: 1,
        year: 2015,
        month: 1,
        day: 1,
        day_of_week: 4,
        airline: 'AS',
        flight_number: 98,
        tail_number: 'N407AS',
        origin_airport: 'ANC',
        destination_airport: 'SEA',
        scheduled_departure: 5,
        departure_time: 2354,
        departure_delay: -11,
        taxi_out: 21,
        wheels_off: 15,
        scheduled_time: 205,
        elapsed_time: 194,
        air_time: 169,
        distance: 1448,
        wheels_on: 404,
        taxi_in: 4,
        scheduled_arrival: 430,
        arrival_time: 408,
        arrival_delay: -22,
        diverted: 0,
        cancelled: 0,
        cancellation_reason: '',
        air_system_delay: '',
        security_delay: '',
        airline_delay: '',
        late_aircraft_delay: '',
        weather_delay: '',
    }
];

// GET
router.get('flights.show', '/', (ctx) => {
    ctx.body = JSON.stringify(flights);
});

router.get('flights.show', '/:id', (ctx) => {
    const flight = flights.find((flight) => {
        return flight.id === parseInt(ctx.params.id);
    });

    if (flight) {
        ctx.body = JSON.stringify(flight);
    } else {
        ctx.status = 404;
    }
});

// DELETE
router.delete('flights.delete', '/:id', (ctx) => {
    const flight = flights.find((flight) => {
        return flight.id === parseInt(ctx.params.id);
    });

    if (flight) {
        flights.splice(flights.indexOf(flight), 1);
        ctx.status = 204;
    } else {
        ctx.status = 404;
    }
});

// POST (NOT WORKING)
router.post('flights.create', '/', (ctx) => {
    const flight = ctx.request.body;

    if (flight) {
        flights.push(flight);
        ctx.status = 201;
    } else {
        ctx.status = 400;
    }
});

// PUT (NOT WORKING)
router.put('flights.update', '/:id', (ctx) => {
    const flight = flights.find((flight) => {
        return flight.id === parseInt(ctx.params.id);
    });

    if (flight) {
        flight.year = ctx.request.body.year;
        ctx.body = JSON.stringify(flight);
    } else {
        ctx.status = 404;
    }
});



module.exports = router;