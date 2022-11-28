import Koa from 'koa';
import KoaBody from 'koa-body';
import KoaLogger from 'koa-logger';
import router from './routes.js';

const app = new Koa();

// app.use(KoaBody());
app.use(KoaLogger());

// app.use((ctx, next) => {
//     ctx.body = 'Hello World';
// });

app.use(router.routes());

app.listen(3000, () => {
    console.log('Server is running on port 3000');
}
);