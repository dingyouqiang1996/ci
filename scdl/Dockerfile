FROM python:3.12
USER root
RUN apt update -y && apt install -y ffmpeg libavcodec-extra && python3 -m pip install scdl && mkdir -p /root/.config/scdl
# COPY cookie /root/.config/scdl/scdl.cfg
CMD ["scdl"]
