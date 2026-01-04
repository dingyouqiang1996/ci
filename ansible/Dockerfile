FROM ccr.ccs.tencentyun.com/panfulu/rasp:ansible-v2
COPY hosts /app/hosts
ENV ANSIBLE_HOST_KEY_CHECKING=False
CMD ["ansible", "rasp", "-i", "/app/hosts", "-f", "4", "-m", "shell", "-a", "poweroff"]