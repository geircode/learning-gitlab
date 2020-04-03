FROM python:3.6 as filedownloader

# RUN apt-get update

WORKDIR /files
# Makes it possible to run Docker Commands from inside the Container to the Docker Host
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-19.03.2.tgz && tar --strip-components=1 -xvzf docker-19.03.2.tgz -C /usr/local/bin

FROM alpine:latest as filecontainer
WORKDIR /files
COPY --from=filedownloader /files .

ENTRYPOINT tail -f /dev/null

