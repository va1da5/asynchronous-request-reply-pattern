.PHONY: help restart

help:
	echo "*"

restart:
	docker-compose rm -sf api worker
	docker-compose up -d  api worker
