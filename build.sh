#!/bin/bash

# set -x

## This deploy options should be used in bamboo only
#if [ "$1" = "deploy" ]; then
#cat > pypirc <<EOF
#[distutils]
#index-servers = otxb_core_library
#[otxb_core_library]
#repository: https://alienvault.jfrog.io/alienvault/api/pypi/otxb-core
#username: ${ARTIFACTORY_USER:=${DEFAULT_ARTIFACTORY_USER}}
#password: ${ARTIFACTORY_PWD:=${DEFAULT_ARTIFACTORY_PWD}}
#EOF
#fi

docker-compose build av-agent-utils-test

# You can use -X for a more verbose output (includes coverage lines)
docker-compose run -w /av-agent-utils \
                   av-agent-utils-test \
                   pyb install_dependencies publish -v

if [ "$1" = "deploy" ]; then
        docker-compose run -w /av-agent-utils \
                   -v $(pwd)/pypirc:/root/.pypirc \
                   av-agent-utils-test \
                   pyb install_dependencies \
                       package \
                       install \
                       upload
fi

docker-compose down -v --rmi local --remove-orphans
#docker rmi av-agent-utils:$TAG
