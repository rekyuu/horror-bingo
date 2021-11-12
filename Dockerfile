FROM python:3.9.7-alpine AS base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "waitress-serve", "--port=5000", "--call", "app:create_app" ]