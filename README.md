# Elasticsearch in Python/Django


# Configurations

- Set up the docker container. This means adding the below configuration to the docker-compose.yml
```
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/usr/src/app/
    ports:
      - "8000:8000"

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.15.0
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"

```
- This will enable the elastic search container and the django with sqlite db
- Copy the below to the requirements.txt
```
asgiref==3.5.2
Django==4.1.2
djangorestframework
future==0.18.2
pytz==2022.5
serializers==0.2.4
sqlparse==0.4.3
django-elasticsearch-dsl==8.0
django-elasticsearch-dsl-drf==0.22.5
```
- docker-compose build
- docker-compose up
- you will be able to see the Elasticsearch running in the URL : http://localhost:9200/
- Add below to Django installed apps
```
INSTALLED_APPS = [
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
]
```
- Create an app and add a models which you wanted to use for elasticsearch index
- docker-compose exec web python manage.py search_index --rebuild
