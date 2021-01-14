FROM python:latest

WORKDIR /service1

COPY . .

RUN ["python", "-m", "pip3", "install", "requests"]

RUN ["pip3", "install", "-r", "requirements.txt"]

EXPOSE 5000

CMD ["python", "app.py"]
