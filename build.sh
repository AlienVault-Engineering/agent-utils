#!/bin/bash

# set -x

docker-compose build av-agent-utils-test

# You can use -X for a more verbose output (includes coverage lines)
docker-compose run -w /av-agent-utils av-agent-utils-test pyb install_dependencies publish -v

if [ "$1" = "deploy" ]; then
    docker-compose run -w /av-agent-utils av-agent-utils-test ./deploy.sh
fi

docker-compose down -v --rmi local --remove-orphans
#docker rmi av-agent-utils:$TAG
