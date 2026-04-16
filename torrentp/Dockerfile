FROM hkccr.ccs.tencentyun.com/rasp/ci:debian_arm64_bullseye

RUN sed -i 's|http://mirrors.aliyun.com|http://deb.debian.org|g' /etc/apt/sources.list && mkdir -p /app && apt update -y && apt install -y python3 python3-pip && python3 -m pip install torrentp
WORKDIR /app

ENTRYPOINT ["torrentp", "--link"]
