const Router = require('koa-router');

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


// GET 
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

// DELETE
router.delete('airlines.delete', '/:iata_code', (ctx) => {
    const airline = airlines.find((airline) => {
        return airline.iata_code === ctx.params.iata_code;
    });

    if (airline) {
        const index = airlines.indexOf(airline);
        airlines.splice(index, 1);
        ctx.status = 204;
    } else {
        ctx.status = 404;
    }
});

// POST (NOT WORKING)
router.post('airlines.create', '/', (ctx) => {
    const airline = ctx.request.body;

    if (airline) {
        airlines.push(airline);
        ctx.status = 201;
    } else {
        ctx.status = 400;
    }
});


// PUT (NOT WORKING)
router.put('airlines.update', '/:iata_code', (ctx) => {
    const airline = airlines.find((airline) => {
        return airline.iata_code === ctx.params.iata_code;
    });

    if (airline) {
        airline.name = ctx.request.body.name;
        ctx.body = JSON.stringify(airline);
    } else {
        ctx.status = 404;
    }
});


module.exports = router;