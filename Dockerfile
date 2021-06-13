# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create scripts folder
RUN mkdir /Volumes
RUN mkdir /Volumes/scripts


# copy start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# install dependencies
RUN pip install -U pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .
