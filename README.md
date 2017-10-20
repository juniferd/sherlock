# sherlock-project

full stack project using Vue.js, flask, SQLAlchemy

## Build Setup

```
# install dependencies
cd web
npm install
cd ../backend
pip install -r backend/requirements.txt

# build for production with minification
# from web/ directory (this will build assets in backend/static/ and backend/templates
cd web
npm run build
```

## init db
```
python backend/init.py
```

## Run server

```
python backend/server.py
```

## Frontend-specific

``` bash
# serve with hot reload at localhost:8080
# from web/ directory
npm run dev

# build for production and view the bundle analyzer report
# from web/ directory 
npm run build --report

# run frontend unit tests
# from web/ directory 
npm run unit

# run e2e tests
# from web/ directory 
npm run e2e

# run all tests
# from web/ directory 
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
