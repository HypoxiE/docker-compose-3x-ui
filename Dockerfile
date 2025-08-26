FROM alpine:3.18

RUN apk add --no-cache bash curl tar ca-certificates

WORKDIR /opt/3x-ui

RUN curl -Ls https://github.com/mhsanaei/3x-ui/releases/download/v2.6.6/x-ui-linux-amd64.tar.gz | tar xz --strip-components=1 \
    && chmod +x x-ui

CMD ["./x-ui"]
