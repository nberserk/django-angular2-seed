FROM nberserk/docker-django-node:latest

# install our code
RUN mkdir /code
copy . /code

# angular
WORKDIR /code/angular-seed
run npm install && npm run build.prod \
    && rm -rf node_modules

# django
WORKDIR /code/api
run pip install -r requirements.txt \
    && python manage.py collectstatic --noinput

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /code/.docker/nginx.conf /etc/nginx/sites-enabled/ \
    && ln -s /code/.docker/supervisor-app.conf /etc/supervisor/conf.d/

expose 80
cmd ["supervisord", "-n"]
