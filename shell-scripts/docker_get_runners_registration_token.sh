#!/bin/bash
docker exec gitlab-server mkdir -p /app
docker cp /app/shell-scripts/get_runners_registration_token.sh gitlab-server:/app/get_runners_registration_token.sh
docker exec gitlab-server /app/get_runners_registration_token.sh