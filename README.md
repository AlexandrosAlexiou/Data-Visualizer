# Data Visualizer

## Application UI

The application UI was built using [Angular Material](https://material.angular.io/guide/getting-started). <br>
The charts were rendered using the [ngx-charts](https://github.com/swimlane/ngx-charts) framework. <br>

![Sample Graph](https://github.com/AlexandrosAlexiou/Statify/blob/master/src/assets/sample-graph.png)

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`.<br/> The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. <br> You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. <br> The build artifacts will be stored in the `dist/` directory. <br> Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

<br/>


# [Node.js](https://nodejs.org/en/download/) API

The API connects to the database and serves the data to our Angular app. <br>

Run `node server.js` to start the service. <br>

v12.16.1
### [npm](https://www.npmjs.com/) packages used
- [mysql](https://www.npmjs.com/package/mysql)

- [cors](https://www.npmjs.com/package/cors)

- [express](https://www.npmjs.com/package/express) ( official website [here](https://expressjs.com/) )

- [moment](https://momentjs.com) (used in the logger middleware function)

<br>

## Run the backend on [Docker](https://www.docker.com)

### Installation
Requirements
- You need to have [**Docker**](https://www.docker.com/get-started) installed

- Run in the `api` folder to build the Node.js - express app image.
    ~~~~
    docker build -t statify/api .
    ~~~~

- Then deploy the system.
    ~~~~
    docker-compose up
    ~~~~

<br>

# ETL process

### The data from the [World Bank dataset](https://data.worldbank.org/country) were normalized accordingly to comply with the Database schema.


### Python packages used

- [PyMySQL](https://pypi.org/project/PyMySQL/) (v0.9.3)
- [openpyxl](https://pypi.org/project/openpyxl/) (v3.0.3)
- [csv](https://docs.python.org/3/library/csv.html)
