import os
import random
import sys

with open("docker-compose.yml", "w+") as file:
	name = os.getlogin()
	if "--ui_p" in sys.argv:
		ui_port = sys.argv[sys.argv.index("--ui_p") + 1]
	else:
		ui_port = input("Укажите порт для ui: ")

	if "--client_p" in sys.argv:
		inp_ports = sys.argv[sys.argv.index("--client_p") + 1]
	else:
		inp_ports = input("Укажите порты для проксирования через пробел в формате 'host_port:docker_port' или просто 'host_port'\n: ")
		
	f_list_ports = []
	list_ports: set[int] = {int(ui_port)}
	for port in inp_ports.split(" "):
		if ":" in port:
			if list_ports & {int(port.split(":")[1])}:
				raise ValueError(f"Некоторые порты в докере повторяются ({int(port.split(":")[1])})")
			f_list_ports.append(f"      - {port}")
			list_ports.add(int(port.split(":")[1]))
		else:
			new_port = int(ui_port)
			while new_port in list_ports:
				new_port = random.randint(10_000, 65_536)
			f_list_ports.append(f"      - {port}:{new_port}")
			list_ports.add(new_port)

	print("Готово! Теперь вы сможете использовать клиентов на следующих портах:", ", ".join(str(i) for i in list_ports ^ {int(ui_port)}))

	file.write('''
services:
  {name}-3x-ui:
    build: .
    container_name: {name}-3x-ui
    ports:
      - "{ui_port}:2053" # port for ui
      # client ports
{clients_ports}
    volumes:
      - ./data:/opt/x-ui/db
    restart: always
'''.format(name=name, ui_port=ui_port, clients_ports='\n'.join(f_list_ports)))