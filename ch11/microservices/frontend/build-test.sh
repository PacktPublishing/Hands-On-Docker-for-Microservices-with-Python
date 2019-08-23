VERSION_SHA=8bee3a8b48638c1f184d084dace3015dd9953b5e
VERSION_NAME=v3.7
docker-compose build --build-arg VERSION_NAME=${VERSION_NAME} --build-arg VERSION_SHA=${VERSION_SHA}
docker tag thoughts_frontend:latest thoughts_frontend:${VERSION_NAME}
