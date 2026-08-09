FROM python:3.12.12-slim-trixie
RUN mkdir -p /app && \
  cd /app && \
  wget -c https://cosbrowser.cloud.tencent.com/software/coscli/coscli-linux-arm64 && \
  mv /app/coscli-linux-arm64 && \
  chmod +x /app/coscli-linux-arm64
WORKDIR /app