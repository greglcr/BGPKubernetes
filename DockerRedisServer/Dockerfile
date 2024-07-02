FROM alpine:latest

USER root

COPY shardedRedis.py /src/shardedRedis.py
COPY redis.conf /src/redis.conf

ADD docker-entrypoint.sh /usr/src/app/docker-entrypoint.sh

RUN ["chmod", "+x", "/usr/src/app/docker-entrypoint.sh"]

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]



