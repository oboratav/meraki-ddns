all: build run

build:
	sudo docker build . -t meraki-ddns
run:
	sudo docker run -d meraki-ddns

