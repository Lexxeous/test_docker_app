# Build: $ docker build -t lexxeous/test_docker_app -f Dockerfile .
# Run: $ docker run -p <host_port>:5000 lexxeous/test_docker_app

FROM python:3.6-alpine

RUN pip install flask

COPY . /opt

EXPOSE 5000

WORKDIR /opt

ENTRYPOINT ["python", "app.py"]