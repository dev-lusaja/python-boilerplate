FROM amazonlinux:2017.09

# Install Python, tools

RUN yum -y update && yum -y install \
    python35 \
    python35-pip \
    python35-devel \
    python35-virtualenv \
    git \
    gcc \
    mysql-devel

ENV TZ=America/Lima

ADD resources /resources/
RUN python35 --version

WORKDIR /app
EXPOSE 8000
ENTRYPOINT /resources/runservices.sh
