#!/bin/bash 


[[ ! "$(pwd)" == "/usr/local/dpad_llc/docker/dpad_llc/public_webpage" ]] && \
    exit 1


function containersRunning() {
    containers="$(docker ps -a --format='{{.Names}}' | grep dpad_llc | wc -l)"
    (( $containers > 0 )) && return 0
    return 1
}


if containersRunning; then
    echo -e "\033[1;33mStopping containers\033[0m"
    docker compose down
    docker rmi public_webpage-dpad_llc_home
    docker rmi public_webpage-dpad_llc_api
fi


docker compose up -d

