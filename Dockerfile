#Base Image
FROM python:3.8

#Create and set working directory
RUN mkdir /code /var/log/play /code/static

WORKDIR /code

#Set default environment variables
ENV PYTHONUNBUFFERED 1


ADD requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y git

RUN pip install -r requirements.txt -U

EXPOSE 8000

CMD gunicorn play.wsgi:application --bind 0.0.0.0:8000

# Copy all the code.
COPY . /code/



