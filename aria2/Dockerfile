FROM ubuntu:devel
ENV https_proxy='http://192.168.0.55:7890'
RUN apt update -y && apt install -y aria2 && mkdir -p /app
WORKDIR /app