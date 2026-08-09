FROM python:3.12.12-slim-trixie
RUN apt update -y && \
  apt install -y wget curl && \
  mkdir /app && \
  curl https://cosbrowser.cloud.tencent.com/software/coscli/coscli-linux-arm64 -o /usr/bin/coscli && \
  chmod +x /usr/bin/coscli
WORKDIR /app