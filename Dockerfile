# Build: $ docker build -t lexxeous/test_docker_app -f Dockerfile .

FROM python:3.6-alpine

RUN pip install flask

COPY . /opt

EXPOSE 5000

WORKDIR /opt

ENTRYPOINT ["python", "app.py"]