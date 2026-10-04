FROM alpine:3.20
RUN wget -q https://github.com/etcd-io/etcd/releases/download/v3.4.13/etcd-v3.4.13-linux-arm64.tar.gz -O - \
  | tar xz --strip-components=1 -C /usr/local/bin etcd-v3.4.13-linux-arm64/etcdctl
ENTRYPOINT ["etcdctl"]