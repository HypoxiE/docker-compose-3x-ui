# файл для инициализации docker-compose.yml

import os
import random
import sys

with open("docker-compose.yml", "w+") as file:
	name = os.getlogin()

	file.write('''
services:
  {name}-3x-ui:
    build: .
    hostname: hypoxie-xui.duckdns.org
    container_name: {name}-3x-ui
    volumes:
      - ./data:/opt/x-ui/db
      - /etc/letsencrypt/:/etc/letsencrypt/:rw
    environment:
      XRAY_VMESS_AEAD_FORCED: "false"
    tty: true
    networks:
      - nginx_network_external
    restart: unless-stopped

networks:
  nginx_network_external:
    external: true
'''.format(name=name))