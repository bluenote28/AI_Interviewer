FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

ENV FLASK_APP=app.py

CMD ["flask", "--app", "main", "run"]