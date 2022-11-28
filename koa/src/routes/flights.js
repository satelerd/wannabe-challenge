// import Router from 'koa-router';

// const router = new Router();

// const airports = [
//     {
//         iata_code: 'ABE',
//         airport: 'Lehigh Valley International Airport',
//         city: 'Allentown',
//         state: 'PA',
//         country: 'USA',
//         latitude: 40.652083,
//         longitude: -75.440806,
//     },
//     {
//         iata_code: 'ABI',
//         airport: 'Abilene Regional Airport',
//         city: 'Abilene',
//         state: 'TX',
//         country: 'USA',
//         latitude: 32.411319,
//         longitude: -99.681897,
//     }
// ];

// // GET /airports
// router.get('airports.show', '/', (ctx) => {
//     ctx.body = JSON.stringify(airports);
// });

// router.get('airports.show', '/:iata_code', (ctx) => {
//     const airport = airports.find((airport) => {
//         return airport.iata_code === ctx.params.iata_code;
//     });

//     if (airport) {
//         ctx.body = JSON.stringify(airport);
//     } else {
//         ctx.status = 404;
//     }
// });

// export default router;


//  ----------------------------------------------------
// write the same but for flights

import Router from 'koa-router';

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

// GET /flights
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

export default router;