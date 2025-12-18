NAME="webserv-docker-siege"

all: build run

build:
	docker build ./srcs/ --tag=$(NAME)

run:
	docker run -ti $(NAME)
