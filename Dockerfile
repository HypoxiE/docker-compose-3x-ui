# FROM debian:stable-slim

# # Установим утилиты для скачивания и распаковки
# RUN apt-get update && apt-get install -y wget tar ca-certificates \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /opt/x-ui

# # Скачиваем и распаковываем конкретный релиз
# RUN wget https://github.com/MHSanaei/3x-ui/releases/download/v2.6.6/x-ui-linux-amd64.tar.gz \
#     && tar -xvf x-ui-linux-amd64.tar.gz --strip-components=1 \
#     && rm x-ui-linux-amd64.tar.gz \
#     && chmod +x x-ui

# CMD ["./x-ui"]

FROM alpine:3.18

RUN apk add --no-cache bash curl tar ca-certificates

WORKDIR /opt/3x-ui

RUN curl -Ls https://github.com/mhsanaei/3x-ui/releases/download/v2.6.6/x-ui-linux-amd64.tar.gz | tar xz --strip-components=1 \
    && chmod +x x-ui

EXPOSE 2053
CMD ["./x-ui"]
