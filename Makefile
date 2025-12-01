NAME="Webserv-Docker-Siege"

all: build run

build:
	docker build ./srcs/ --tag=$(NAME)

run:
	docker run -ti main