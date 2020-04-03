cd %~dp0
docker-compose -f filecontainer/docker-compose.yml build
docker-compose -f docker-compose.yml build
pause
