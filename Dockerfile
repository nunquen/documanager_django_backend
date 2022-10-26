FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python3-pip python3-dev python3.8-venv libssl-dev wget bzip2 \
                    libsecp256k1-dev software-properties-common dnsutils \
                    apt-utils xmlsec1 sqlite3 libsqlite3-dev sudo bash-completion -y

#FROM python:3.8
# Installing environment
RUN useradd -u 1001 -s /bin/bash propylon
ENV VIRTUAL_ENV=/opt/venv
RUN mkdir $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m pip install --upgrade pip
RUN python3 -m venv $VIRTUAL_ENV
RUN chmod +x $VIRTUAL_ENV/bin/activate

#RUN su - propylon
#ENV VIRTUAL_ENV=/opt/venv
#RUN source $VIRTUAL_ENV/bin/activate

# Installing requirements
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /propylon
COPY requirements.txt .
COPY docker_ini.sh .
COPY manage.py .
COPY documanager/ /propylon/documanager/
RUN python3 -m pip install -r requirements.txt

ENV DJANGO_SUPERUSER_PASSWORD=admin.123
ENV DJANGO_SUPERUSER_EMAIL=admin@documanager.com
ENV DJANGO_SUPERUSER_USERNAME=admin

RUN chmod +x /propylon/docker_ini.sh
ENTRYPOINT [ "/propylon/docker_ini.sh" ]
