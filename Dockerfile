FROM debian:stable-slim

# Установим утилиты для скачивания и распаковки
RUN apt-get update && apt-get install -y wget tar ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/3x-ui

# Скачиваем и распаковываем конкретный релиз
RUN wget https://github.com/MHSanaei/3x-ui/releases/download/v1.8.3/3x-ui-linux-amd64.tar.gz \
    && tar -xvf 3x-ui-linux-amd64.tar.gz --strip-components=1 \
    && rm 3x-ui-linux-amd64.tar.gz \
    && chmod +x 3x-ui

EXPOSE 54321

CMD ["./3x-ui"]
