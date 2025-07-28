FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

ENV FLASK_APP=app.py

ARG GEMINI_API_KEY
ENV GEMINI_API_KEY=$GEMINI_API_KEY

CMD ["python3", "main.py"]