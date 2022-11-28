import Router from 'koa-router';

const router = new Router();

const airlines = [
    {
        id: 1,
        iata_code: 'AA',
        name: 'American Airlines',
    },
    {
        id: 2,
        iata_code: 'BA',
        name: 'British Airways',
    }
];


// GET /airlines
router.get('airlines.show', '/', (ctx) => {
    ctx.body = JSON.stringify(airlines);
});

router.get('airlines.show', '/:iata_code', (ctx) => {
    const airline = airlines.find((airline) => {
        return airline.iata_code === ctx.params.iata_code;
    });

    if (airline) {
        ctx.body = JSON.stringify(airline);
    } else {
        ctx.status = 404;
    }
});

// router.post('airlines.create', '/', (ctx) => {
//     const airline = ctx.request.body;

//     if (airline) {
//         airlines.push(airline);
//         ctx.status = 201;
//     } else {
//         ctx.status = 400;
//     }
// });


export default router;