cd %~dp0

call docker-compose.build.all.bat
call docker-compose.up.bat

pause
docker exec -it learning_gitlab-1 /bin/bash