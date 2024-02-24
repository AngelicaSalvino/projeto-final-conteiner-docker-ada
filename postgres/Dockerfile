FROM postgres:14

RUN echo "CREATE USER postgres;" | docker-entrypoint.sh
RUN echo "CREATE DATABASE postgres;" | docker-entrypoint.sh
RUN echo "GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;" | docker-entrypoint.sh

COPY create.sql /docker-entrypoint-initdb.d/
