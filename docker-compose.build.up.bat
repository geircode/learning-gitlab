cd %~dp0


set DOCKER_LATEST_VERSION_FILE=docker-19.03.4.tgz

call docker-compose.build.all.bat
call docker-compose.up.bat

pause
docker exec -it learning_gitlab-1 /bin/bash