# Defina a porta desejada
PORT = 1234

all:
	clear
	python3 class_lib/Server.py
	sleep 5
	lsof -t -i:$(PORT)

