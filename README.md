# django-angular2-seed
seed project for angular2 and django

## setup


```bash
$ git clone https://github.com/nberserk/django-angular2-seed
$ cd django-angular2-seed

```

### dev setup

for development setup, follow following setps:


```bash
# run Django rest framework
$ cd api
$ pip install -r requirements
$ ./manage.py runserver

# run Angular2 app
$ cd ../angular-seed
$ npm install # first time only
$ npm start

```

check this url for django api server : http://localhost:8000

check this url for angular2 app :  http://localhost:5555




### Dockerization

Are you ready to deploy your app? then you can deploy your app using docker image.

```bash
$ cd django-angular2-seed
$ docker-compose build --pull
$ docker-compose up -d
$ docker exec web ./manage.py migrate

# then access to http://localhost:80/api/people , and add some peoples.
# then access to http://localhost:80 , then you can see added people list there.

```

now your docker image is running locally. check http://localhost:80



### Credit

- Frontend seed - slightly modified version of [mgechev/angular2-seed](https://github.com/mgechev/angular-seed)

