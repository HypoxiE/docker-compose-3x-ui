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
    container_name: {name}-3x-ui
    volumes:
      - ./data:/opt/x-ui/db
    networks:
      - nginx_network_external
    restart: always

networks:
  nginx_network_external:
    external: true
'''.format(name=name))