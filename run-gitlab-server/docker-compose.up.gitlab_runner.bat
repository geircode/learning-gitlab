cd %~dp0
docker rm -f gitlab_runner1
docker-compose -f docker-compose.yml up -d gitlab_runner1
REM wait for 1-2 seconds for the container to start
pause
docker exec -it gitlab_runner1 /bin/bash