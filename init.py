# файл для инициализации docker-compose.yml

import os
import random
import sys

with open("docker-compose.yml", "w+") as file:
	name = os.getlogin()
	# if "--ui_p" in sys.argv:
	# 	ui_port = sys.argv[sys.argv.index("--ui_p") + 1]
	# else:
	# 	ui_port = input("Укажите порт для ui: ")

	if "--client_p" in sys.argv:
		inp_ports = sys.argv[sys.argv.index("--client_p") + 1]
	else:
		inp_ports = input("Укажите порты для проксирования через пробел в формате 'host_port'\n: ")
		
	f_list_ports = []
	for port in inp_ports.split(" "):
		f_list_ports.append(f"      - {port}:{port}")

	print("Готово!")

	file.write('''
services:
  {name}-3x-ui:
    build: .
    container_name: {name}-3x-ui
    volumes:
      - ./data:/opt/x-ui/db
      - /etc/letsencrypt/:/etc/letsencrypt/:rw
    environment:
      XRAY_VMESS_AEAD_FORCED: "false"
    ports:
{f_list_ports}
    tty: true
    networks:
      - nginx_network_external
    restart: unless-stopped

networks:
  nginx_network_external:
    external: true
'''.format(name=name, f_list_ports="\n".join(f_list_ports)))