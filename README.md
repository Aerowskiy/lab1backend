# Посилання на сайт

https://lab1backend-hwom.onrender.com

# Щоб запустити у себе на пк 

1. Клонувати репозиторій;
2. Віртуальне середовища:
```
python3 -m venv env
```
3. Активація:
```
source ./env/bin/activate
```
4. Встановити залежності:
```
pip install -r requirements.txt
```
5. Build image:
```
docker build --build-arg PORT=<your port> . -t <image_name>:latest
```
6. Run image
```
docker run -it --rm --network=host -e PORT=<your port> <image_name>:latest
```
7. DOCKER_COMPOSE container build:
```
docker-compose build
```
8. DOCKER_COMPOSE container run:
```
docker-compose up
```
