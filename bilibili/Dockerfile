FROM python:3.12.12-trixie
COPY requirements.txt requirements.txt
RUN echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian/ trixie main contrib non-free non-free-firmware' > /etc/apt/sources.list && \
  echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian/ trixie-updates main contrib non-free non-free-firmware' >> /etc/apt/sources.list && \
  echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian/ trixie-backports main contrib non-free non-free-firmware' >> /etc/apt/sources.list && \
  echo 'deb https://security.debian.org/debian-security trixie-security main contrib non-free non-free-firmware' >> /etc/apt/sources.list && \
  apt update -y && \
  apt install -y ffmpeg git && \
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip && \
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
  mkdir /app && \
  cd /app && \
  git clone https://github.com/tyokyo320/bilibili-downloader.git
COPY config.py /app/bilibili-downloader/config.py
COPY main.py /app/bilibili-downloader/main.py
COPY bilibili_executor.py /app/bilibili-downloader/strategy/bilibili_executor.py
WORKDIR /app/bilibili-downloader
CMD ["python3.12", "main.py"]