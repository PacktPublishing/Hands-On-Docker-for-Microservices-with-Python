# This Dockerfile is for localdev purposes only, so it won't be
# optimised for size
FROM alpine:3.9

# Add the proper env variables for init the db
ARG POSTGRES_DB
ENV POSTGRES_DB $POSTGRES_DB
ARG POSTGRES_USER
ENV POSTGRES_USER $POSTGRES_USER
ARG POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
ARG POSTGRES_PORT

# For usage in startup, etc
ENV POSTGRES_HOST localhost

RUN apk update
RUN apk add bash nano curl su-exec python3
RUN apk add postgresql postgresql-contrib postgresql-dev
RUN apk add python3-dev build-base linux-headers gcc libffi-dev

### Adding musl with locale support for Postgres

# set our environment variable
ENV MUSL_LOCPATH="/usr/share/i18n/locales/musl"

# install libintl
# then install dev dependencies for musl-locales
# clone the sources
# build and install musl-locales
RUN apk --no-cache add libintl && \
	apk --no-cache --virtual .locale_build add cmake make musl-dev gcc gettext-dev git && \
	git clone https://gitlab.com/rilian-la-te/musl-locales && \
	cd musl-locales && cmake -DLOCALE_PROFILE=OFF -DCMAKE_INSTALL_PREFIX:PATH=/usr . && make && make install

ENV LANG en_US.utf8
ENV PGDATA /var/lib/postgresql/data

# ENTRYPOINT ["/postgres-entrypoint.sh"]

EXPOSE $POSTGRES_PORT
VOLUME /var/lib/postgresql/data

# Adding our code
RUN mkdir -p /opt/code
RUN mkdir -p /opt/data

# Store the data inside the container, as we don't care for
# persistence
ENV PGDATA /opt/data
WORKDIR /opt/code

RUN mkdir -p /opt/code/db
# Add postgres setup
ADD ./docker/db/postgres-setup.sh /opt/code/db/
RUN  /opt/code/db/postgres-setup.sh

## Install our code to prepare the DB
ADD ./ThoughtsBackend/requirements.txt /opt/code

RUN pip3 install -r requirements.txt

## Need to import all the code, due dependencies to initialise the DB
ENV DATABASE_ENGINE POSTGRESQL
ADD ./ThoughtsBackend/ /opt/code/
# Add all DB commanda
ADD ./docker/db/* /opt/code/db/

## get the db ready
RUN /opt/code/db/prepare_db.sh

CMD ["su-exec",  "postgres", "postgres"]
