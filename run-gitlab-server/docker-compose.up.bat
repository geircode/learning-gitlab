cd %~dp0
docker rm -f gitlab_ee-1
docker rm -f gitlab_runner1-1
docker-compose -f docker-compose.yml down --remove-orphans
docker-compose -f docker-compose.yml pull --no-parallel
docker-compose -f docker-compose.yml up -d --remove-orphans
REM wait for 1-2 seconds for the container to start
pause
docker exec -it gitlab_runner1-1 /bin/bash