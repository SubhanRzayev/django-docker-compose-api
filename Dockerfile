FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code
COPY requirements.txt ./


RUN pip install -r requirements.txt
COPY  . .


CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000", "Blog.wsgi" ]









