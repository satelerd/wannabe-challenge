/* eslint no-console: "off" */

const app = require('./app');
const orm = require('./models');

const port = process.env.PORT || 3000;

orm.sequelize
    .authenticate()
    .then(() => {
        console.log('Connection has been established successfully.');
        app.listen(port, (err) => {
            if (err) {
                return console.log(err);
            }
            console.log(`Server is running on port ${port}`);
            return app;
        });
    })
    .catch((err) => console.error('Unable to connect to the database:', err));
