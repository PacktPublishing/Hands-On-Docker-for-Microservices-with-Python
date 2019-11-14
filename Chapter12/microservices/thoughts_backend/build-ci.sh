#!/bin/bash
if [ -z "$1" ]
  then
    # Error, not version name
    echo "No VERSION_NAME supplied"
    exit -1
fi

VERSION_SHA=`git log --format=format:%H -n 1`
VERSION_NAME=$1

echo "Building version \"${VERSION_NAME}\""

docker-compose build --build-arg VERSION_NAME=${VERSION_NAME} --build-arg VERSION_SHA=${VERSION_SHA}

# tag the resulting image with the version
docker tag thoughts_server:latest thoughts_server:${VERSION_NAME}
