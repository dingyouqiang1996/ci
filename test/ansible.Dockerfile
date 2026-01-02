FROM ubuntu:22.04
RUN apt update -y && apt install -y openssh-client ansible && mkdir /app 
WORKDIR /app
