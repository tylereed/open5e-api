FROM python:3.11-alpine

RUN mkdir -p /opt/services/open5e-api
WORKDIR /opt/services/open5e-api
# copy our project code

# install our dependencies
RUN pip install pipenv
COPY . /opt/services/open5e-api
RUN pipenv install --system --deploy

# migrate the db, load content, and index it
RUN python manage.py quicksetup

# remove .env file (set your env vars via docker-compose.yml or your hosting provider)
RUN rm .env

#run gunicorn.
CMD ["gunicorn","-b", ":8888", "server.wsgi:application"]
