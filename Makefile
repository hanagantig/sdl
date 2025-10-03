dump:
	./manage.py dumpdata > data_dump.json

loaddata:
	./manage.py loaddata data_dump.json

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate