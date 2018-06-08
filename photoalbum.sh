#!/bin/bash

sudo docker-compose up --build -d
sudo docker-compose run albums-service python manage.py recreate_db
sudo docker-compose run albums-service python manage.py seed_db
