#!/bin/sh
docker-compose down --volumes --remove-orphans
docker system prune --force
docker volume prune --force
docker ps
docker volume ls