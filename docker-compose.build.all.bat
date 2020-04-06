cd %~dp0

set DOCKER_LATEST_VERSION_FILE=docker-19.03.4.tgz

docker-compose -f filecontainer/docker-compose.yml build --no-cache
docker-compose -f docker-compose.yml build --no-cache

pause
