FROM hkccr.ccs.tencentyun.com/rasp/ci:debian_arm64_bulleye

RUN mkdir -p /app && apt update -y && apt install -y python3 && python3 -m pip install torrentp
WORKDIR /app

ENTRYPOINT ["torrentp", "--link"]
