FROM python:3.10-slim-buster

LABEL maintainer="petr.bezza.bezousek@gmail.com"

WORKDIR /www/WineStorage

COPY requirements.txt .

# gcc because uwsgi https://stackoverflow.com/questions/47868161/failed-building-wheel-for-uwsgi
# git because pre commit hook for new alembic revision
RUN apt-get update && apt-get install -y gcc git && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4321

CMD ["uwsgi", "/www/WineStorage/uwsgi.ini", "--set-placeholder", "port=4321"]
