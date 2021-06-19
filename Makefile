

.PHONY: docker docker_build docker_run
docker: docker_build docker_run
docker_build:
	time docker build -f Dockerfile -t yoga_graph .
docker_run:
	docker run -it --user $$(id -u):$$(id -g) -v `pwd`:/scratch -w /scratch --rm yoga_graph /bin/bash


black:
	black src/*.py
