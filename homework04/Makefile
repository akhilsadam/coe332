NAME = akhilsadam

all: clean build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

clean:
	rm code/__pycache__/ -r
	rm code/.pytest_cache/ -r

build:
	docker build -t ${NAME}/ml_data_analysis:hw04 .
	docker run -it --rm ${NAME}/ml_data_analysis:hw04 pytest code

run:
	docker run --rm ${NAME}/ml_data_analysis:hw04 land.py data/data.json

push:
	docker login docker.io
	docker push ${NAME}/ml_data_analysis:hw04