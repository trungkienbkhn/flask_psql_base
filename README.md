# Flask psql base

## Environment

- Python3

## Project requirements

- Flask
- PostgreSQL

## Project setup

- Create .env

```
cp .env.example .env
```

- Run docker

```
docker-compose up -d
```

- Create venv

```
python3 -m venv venv
```

- Launch venv

```
source venv/bin/activate
```

- Install pip packages

```
pip3 install -r requirements.txt
```

- Start server

```
flask run
```
