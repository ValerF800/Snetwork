FROM python:3.9-alpine


WORKDIR /djsite
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# CMD gunicorn -b 188.130.251.2 Snetwork.wsgi:application
CMD gunicorn -b 0.0.0.0:8000 Snetwork.wsgi:application