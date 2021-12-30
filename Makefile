bot_stop:
	docker-compose -f compose/docker-compose.yml down

bot_start:
	docker-compose -f compose/docker-compose.yml build bot_api && docker-compose -f compose/docker-compose.yml up

bot_restart:
	docker-compose -f compose/docker-compose.yml down && docker-compose -f compose/docker-compose.yml build bot_api && docker-compose -f compose/docker-compose.yml up
