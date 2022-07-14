## Configuration system environments
`export PYTHONPATH=$PWD`
## Start all services
`docker-compose up -d`
## Run server
`flask run`
## Run tests
`pytest --variables tests/dev-test.json tests/[file_name]`

with [file_name] is test file in `tests` folder that you want to run
