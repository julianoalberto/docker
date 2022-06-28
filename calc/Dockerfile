FROM python:3.8-alpine

WORKDIR /app

COPY calc.py /app

RUN pip install flask

ENV FLASK_APP=calc

ENTRYPOINT ["flask", "run"]
