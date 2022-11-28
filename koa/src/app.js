const Koa = require('koa');
const KoaBody = require('koa-body');
const KoaLogger = require('koa-logger');
const router = require('./routes.js');
const orm = require('./models');

const app = new Koa();

// app.use(KoaBody());
app.use(KoaLogger());

// expose orm to context
app.context.orm = orm;

// app.use((ctx, next) => {
//     ctx.body = 'Hello World';
// });

app.use(router.routes());

app.listen(3000, () => {
    console.log('Server is running on port 3000');
}
);

module.exports = app;