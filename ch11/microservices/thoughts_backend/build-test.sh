VERSION_SHA=8bee3a8b48638c1f184d084dace3015dd9953b5e
VERSION_NAME=v1.5
docker-compose build --build-arg VERSION_NAME=${VERSION_NAME} --build-arg VERSION_SHA=${VERSION_SHA}
docker tag thoughts_server:latest thoughts_server:${VERSION_NAME}
