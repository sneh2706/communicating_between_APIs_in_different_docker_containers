FROM python:latest

WORKDIR /service2

COPY . .

RUN ["python", "-m", "pip3", "install", "requests"]

RUN ["pip3", "install", "-r", "requirements.txt"]

EXPOSE 5001

CMD ["python", "app.py"]
