FROM python:3.10-slim-bullseye

ADD ./requirements.txt /app/requirements.txt

ADD . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "subscription.wsgi:application"]

# Render wan kill me