FROM --platform=linux/arm64 alpine:3.24
RUN mkdir -p /app && \
  cd /app && \
  apk add --no-cache curl ca-certificates && \
  curl -fL https://cosbrowser.cloud.tencent.com/software/coscli/coscli-linux-arm64 -o /usr/bin/coscli-linux-arm64 && \
  mv /usr/bin/coscli-linux-arm64 /usr/bin/coscli && \
  chmod +x /usr/bin/coscli
WORKDIR /app
