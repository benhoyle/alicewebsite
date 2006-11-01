# Pull base image.
FROM aarch64/python:2.7-alpine

ENV INSTALL_PATH /alicewebsite
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "python:config.gunicorn" "alicehoyle.app:create_app()"