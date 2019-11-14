VERSION_SHA=2f2d3214e35ea13eeb8655c490323a83df22f6d2
VERSION_NAME=v2.3
docker-compose build --build-arg VERSION_NAME=${VERSION_NAME} --build-arg VERSION_SHA=${VERSION_SHA}

# tag the resulting image with the version
docker tag users_server:latest users_server:${VERSION_NAME}
