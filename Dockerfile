FROM python:3.7.4-stretch
MAINTAINER Vizzuality info@vizzuality.com

ENV NAME recentimagery
ENV USER recentimagery

RUN apt-get update -qqy && apt-get install -qqy \
   bash\
   git\
   libssl-dev\
   libffi-dev\
   gcc\
   python-dev\
   musl-dev\
   libgeos-dev\
   build-essential\
   python-dev

RUN addgroup $USER
# RUN adduser --shell /bin/bash --disabled-password --ingroup $USER
RUN useradd -ms /bin/bash -g $USER $USER

RUN easy_install pip && pip install --upgrade pip
RUN pip install gunicorn gevent setuptools

RUN mkdir -p /opt/$NAME
RUN cd /opt/$NAME
COPY requirements.txt /opt/$NAME/requirements.txt
RUN cd /opt/$NAME && pip install -r requirements.txt


COPY entrypoint.sh /opt/$NAME/entrypoint.sh
COPY main.py /opt/$NAME/main.py
COPY gunicorn.py /opt/$NAME/gunicorn.py
#COPY privatekey.json /opt/$NAME/privatekey.json

# Copy the application folder inside the container
WORKDIR /opt/$NAME

COPY ./$NAME /opt/$NAME/$NAME
COPY ./microservice /opt/$NAME/microservice
#COPY ./tests /opt/$NAME/tests
RUN chown $USER:$USER /opt/$NAME

# Tell Docker we are going to use this ports
EXPOSE 4503
USER $USER

# Launch script
ENTRYPOINT ["./entrypoint.sh"]

