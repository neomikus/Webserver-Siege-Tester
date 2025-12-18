NAME="webserv-docker-siege"

ENV=.env

all: build run

build: $(ENV)
	docker build ./srcs/ --tag=$(NAME)

$(ENV):
	echo "exec_name=" >> .env
	echo "config_file_name=" >> .env
	echo "host=" >> .env
	echo "port=" >> .env
	echo "root_folder=" >> .env

run:
	docker run -ti $(NAME)
