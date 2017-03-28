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




### prod setup

Are you ready to ship your app? then you can deploy your app using docker image easily.

```bash
$ cd django-angular2-seed
$ docker-compose build
$ 

```

now your docker image is 



### Credit

- Frontend seed - slightly modified version of [mgechev/angular2-seed](https://github.com/mgechev/angular-seed)

