#!/bin/bash
BASEDIR=$(dirname "$0")
echo "$BASEDIR"
cd $BASEDIR
docker-compose -f docker-compose.yml pull --no-parallel
docker-compose -f docker-compose.yml up -d --remove-orphans

container_name=gitlab-server

docker inspect -f {{.State.Health.Status}} gitlab-server

sleep_seconds=5

while true; do
    echo "Checking container: $container_name status..."

    output=$(docker inspect -f {{.State.Health.Status}} $container_name)

    echo "docker inspect -f {{.State.Health.Status}} $container_name => $output"
    
    if [ "$output" == "healthy" ]
    then
        echo "$container_name is running and ready to process requests."
        break
    fi

    echo "$container_name is warming up. Trying again in $sleep_seconds seconds..."
    sleep $sleep_seconds
done

python /app/python/gitlab/get_registration_key