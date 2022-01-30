#/usr/bin/env bash

FLASK_APP="wsgi.py" flask db revision --autogenerate --message "${message:-No message}" --directory "src/migrations"
