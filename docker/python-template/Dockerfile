FROM python:3.10-alpine

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./src /app

WORKDIR /app

CMD ["python", "/app/app.py"]