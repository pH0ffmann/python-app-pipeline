FROM python:3.13.1-alpine3.21

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3", "app.py"]