# Django DRF Elasticsearch

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-drf-elasticsearch/).

## Want to use this project?

There are 2 ways you can run the project

[Run with python and installing Elasticsearch](#run-with-python-and-installing-elasticsearch)
[Run with Docker](#run-project-with-docker)
[Testing Elasticsearch](#testings-elasticsearch)

### Run with python and installing Elasticsearch

1. Fork/Clone

2. [Install Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) if you haven't already and make sure it is running on port `9200`.

3. Create and activate a virtual environment:

   ```sh
   $ python3 -m venv venv && source venv/bin/activate
   ```

4. Install the requirements:

   ```sh
   (venv)$ pip install -r requirements.txt
   ```

5. In `core/settings.py` Change value of `RUN_WITH_DOCKER` to `False`.

6. Apply the migrations:

   ```sh
   (venv)$ python manage.py migrate
   ```

7. Populate the database with some test data by running the following command:

   ```sh
   (venv)$ python manage.py populate_db
   ```

8. Create and populate the Elasticsearch index and mapping:

   ```sh
   (venv)$ python manage.py search_index --rebuild
   ```

9. Run the server

   ```sh
   (venv)$ python manage.py runserver
   ```

## Run project with docker

### Requirements:

1. Install docker
2. Install docker-compose

### First Run:

#### Run this command to pull all the necessary images and build image based on Dockerfile:

```sh
docker-compose up --build
```

#### Wait until see the logs of containers like `app` and `kibana`. Then open up another terminal and run:

```sh
docker ps
```

**Note**: All of the containers must be UP at the STATUS column.

#### Connect to the `app` container then Run these commands:

```sh
docker exec -it app bash
```

#### In `app` container's terminal, to topulate the database:

```sh
python manage.py populate_db
```

#### In `app` container's terminal, To Create and populate the Elasticsearch index and mapping:

```sh
python manage.py search_index --rebuild
```

#### To stop the docker containers run:

```sh
docker-compose down
```

#### To start each time after the first time you can run:

```sh
 docker-compose up
```

## Testings Elasticsearch

Test Elasticsearch with the following queries:

- [http://127.0.0.1:8000/search/user/mike/](http://127.0.0.1:8000/search/user/mike/) - should find the user 'mike13'
- [http://127.0.0.1:8000/search/user/jess\_/](http://127.0.0.1:8000/search/user/jess_/) - should find the user 'jess\_'
- [http://127.0.0.1:8000/search/category/seo/](http://127.0.0.1:8000/search/category/seo/) - should find the category 'SEO optimization'
- [http://127.0.0.1:8000/search/category/progreming/](http://127.0.0.1:8000/search/category/progreming/) - should find the category 'Programming' (:warning: notice the typo)
- [http://127.0.0.1:8000/search/article/linux/](http://127.0.0.1:8000/search/article/linux/) - should find the article 'Installing the latest version of Ubuntu'
- [http://127.0.0.1:8000/search/article/java/](http://127.0.0.1:8000/search/article/java/) - should find the article 'Which programming language is the best?'
