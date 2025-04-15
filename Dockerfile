FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "src/app.py"]
