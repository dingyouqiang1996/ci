FROM debian:bullseye

RUN apt-get update -o Acquire::https::Verify-Peer=false && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*
RUN sed -i 's/deb.debian.org/mirrors.tencent.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.tencent.com/g' /etc/apt/sources.list && \
    apt-get update && apt-get install gettext -y && apt-get clean

ENV TZ=Asia/Shanghai LANG=C.UTF-8

WORKDIR /root

CMD ["/bin/bash"]