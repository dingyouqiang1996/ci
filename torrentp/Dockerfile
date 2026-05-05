FROM hkccr.ccs.tencentyun.com/rasp/ci:debian_arm64_bullseye

RUN sed -i 's|http://mirrors.aliyun.com|http://deb.debian.org|g' /etc/apt/sources.list && mkdir -p /app && apt update -y && apt install -y python3 python3-pip proxychains4 && python3 -m pip install torrentp
RUN printf "strict_chain\nproxy_dns\n[ProxyList]\nsocks5 192.168.0.58 7891\n" \
    > /etc/proxychains4.conf
ENV HTTP_PROXY=socks5h://192.168.0.58:7891
ENV HTTPS_PROXY=socks5h://192.168.0.58:7891
ENV ALL_PROXY=socks5h://192.168.0.58:7891

WORKDIR /app

ENTRYPOINT ["proxychains4", "torrentp", "--link"]
