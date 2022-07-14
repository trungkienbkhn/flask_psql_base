FROM ubuntu:20.04
RUN apt-get update -y && apt-get install -y \
            curl python3 python3-pip libssl-dev
RUN python3 -m pip install pip --upgrade
RUN CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" \
    UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi -I --no-cache-dir

RUN mkdir -p /flask_psql_base
WORKDIR /flask_psql_base
COPY server /flask_psql_base/server
COPY requirements.txt /flask_psql_base/

RUN pip install -r requirements.txt

ENV LANG=C.UTF-8
