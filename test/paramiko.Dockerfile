FROM ubuntu:rolling
RUN apt update -y && apt install -y openssh-client python3-pip && pip install paramiko && mkdir /app 
COPY ssh.py /app/ssh.py
WORKDIR /app
ENV password=${password}
CMD python /app/ssh.py
