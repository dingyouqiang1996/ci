FROM python:3.12.12-trixie
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip && \
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
  mkdir /app &&
  git clone https://github.com/tyokyo320/bilibili-downloader.git
WORKDIR /app/bilibili-downloader
