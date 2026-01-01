FROM golang:1.26-rc-bookworm
RUN mkdir /app
COPY ./* /app
RUN cd /app && go mod tidy && go build /app/main.go
WORKDIR /app
CMD /app/main