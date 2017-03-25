# Pull base image.
FROM aarch64/python:2.7-alpine

# Makes a nice tidy working directory
ENV INSTALL_PATH /website
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .