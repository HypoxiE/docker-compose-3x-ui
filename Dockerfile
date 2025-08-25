FROM debian:bullseye-slim

RUN apk add --no-cache bash curl tar ca-certificates

WORKDIR /opt/3x-ui
# username FSGChr9G0x; password mmpwYHix7; port 11111
RUN echo -e "n\n" | bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)

EXPOSE 2053
CMD ["./x-ui"]
