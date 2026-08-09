FROM --platform=linux/arm64 alpine:3.24
RUN mkdir -p /app && \
  cd /app && \
  apk add --no-cache curl ca-certificates && \
  curl -fL https://github.com/minio/mc/releases/download/RELEASE.2025-08-13T08-35-41Z/mc.linux-arm64.RELEASE.2025-08-13T08-35-41Z -o /usr/bin/mc && \
  chmod +x /usr/bin/mc
WORKDIR /app
