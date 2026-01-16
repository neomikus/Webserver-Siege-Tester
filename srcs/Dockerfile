FROM python:3.14

ARG ROOT_FOLDER=www

RUN apt update && apt upgrade -y
RUN apt install -y siege

RUN mkdir -p /app/test

COPY test/webserver/* /app/test/
COPY test/${ROOT_FOLDER} /app/test/${ROOT_FOLDER}
COPY test/tester /app/test/tester

WORKDIR /app/test

CMD ["python3", "./tester/tester.py"]
