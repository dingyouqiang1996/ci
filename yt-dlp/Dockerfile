FROM python:3.12.12-slim-trixie
RUN apt update -y && apt install -y ffmpeg && pip3.12 install yt-dlp -i https://pypi.tuna.tsinghua.edu.cn/simple && mkdir /app && pip3.12 install -U yt-dlp
WORKDIR /app/
# v7_192.168.0.62
ENV http_proxy='http://192.168.0.62:7890'
ENV https_proxy='http://192.168.0.62:7890'
CMD ["yt-dlp"]
