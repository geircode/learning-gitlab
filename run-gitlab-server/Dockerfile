FROM geircode/learning_gitlab-filecontainer:latest as filecontainer

FROM python:3.6

WORKDIR /app
COPY . /app

# RUN pip install -r requirements.txt 

# RUN apt-get update
# RUN apt-get install -y jq

# RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz && tar --strip-components=1 -xvzf docker-17.03.1-ce.tgz -C /usr/local/bin

WORKDIR /files
COPY --from=filecontainer /files .
RUN tar --strip-components=1 -xvzf docker-18.06.1-ce.tgz -C /usr/local/bin
RUN rm *

ENTRYPOINT tail -f /dev/null

