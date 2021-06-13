USERID := $$(id -u)
GROUPID := $$(id -g)

COMPOSE := docker-compose -f docker-compose.yml
COMPOSE_PYTHON := ${COMPOSE} run -u $(USERID):$(GROUPID) --rm django python

up:
	${COMPOSE} up

down:
	${COMPOSE} down

build:
	${COMPOSE} build

build_no_cache:
	${COMPOSE} build --no-cache

create_network:
	docker network create --driver bridge --subnet=172.28.0.0/16 --gateway 172.28.1.1 clutchpoints

collectstatic:
	$(COMPOSE_PYTHON) manage.py collectstatic --noi -c

migrate:
	$(COMPOSE_PYTHON) manage.py migrate ${app}

makemigrations:
	$(COMPOSE_PYTHON) manage.py makemigrations ${app}

createsuperuser:
	$(COMPOSE_PYTHON) manage.py createsuperuser

flush:
	$(COMPOSE_PYTHON) manage.py flush --noinput

shell:
	$(COMPOSE_PYTHON) manage.py shell

test:
	$(COMPOSE_PYTHON) -m pytest -vv

pip_compile:
	pip-compile requirements/base.in
	pip-compile requirements/dev.in
	pip-compile requirements/production.in
	pip-compile requirements/test.in
