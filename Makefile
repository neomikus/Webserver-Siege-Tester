NAME="webserv-docker-siege"

ENV=srcs/.env

all: build run

build: $(ENV)
	docker build ./srcs/ --tag=$(NAME)

$(ENV):
	echo "webserv_exec_name=webserv" >> $(ENV)
	echo "webserv_config_file_name=default.conf" >> $(ENV)
	echo "webserv_host=127.0.0.1" >> $(ENV)
	echo "webserv_port=8080" >> $(ENV)
	echo "webserv_root_folder=www" >> $(ENV)

run:
	docker run --env-file $(ENV) -ti $(NAME)
