FROM ubuntu:22.04
RUN apt update -y && apt install -y openssh-client python3-pip && pip install paramiko && mkdir /app 
COPY ssh.py /app/ssh.py
WORKDIR /app
ENV p ${p}
CMD python /app/ssh.py
