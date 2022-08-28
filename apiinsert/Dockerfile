FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y procps
COPY . /app

ENV FLASK_APP=flask_app.py
ENV PYTHONPATH=/app

EXPOSE 5000
CMD ["flask", "run"]
