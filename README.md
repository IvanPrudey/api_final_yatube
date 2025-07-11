## О проекте:

Yatube — это платформа для блогов. Блог-сервис предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него. Через этот интерфейс смогут работать мобильное приложение или чат-бот; данные через этот API можно будет передавать и на фронтенд.

## Cтек использованных технологий:

```
Python 3
Django 3
REST API (Django REST framework)
Аутентификация по токену, JWT + Djoser
Pytest
```

## Как запустить проект api_final_yatube:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IvanPrudey/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в директорию /yatube_api:

```
cd yatube_api
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация и примеры запросов:

### Получение публикаций

```
GET 
http://127.0.0.1:8000/api/v1/posts/

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

## Создание публикации
```
POST 
http://127.0.0.1:8000/api/v1/posts/
Request samples
{
"text": "string",
"image": "string",
"group": 0
}

Response samples
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

## Получение публикации по id

```
GET
http://127.0.0.1:8000/api/v1/posts/0/

Response samples
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

## Добавление комментария
Добавление нового комментария к публикации. Анонимные запросы запрещены.

```
POST
http://127.0.0.1:8000/api/v1/posts/0/comments/
Request samples
{
  "text": "string"
}

Response samples
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

Подробную документацию и примеры смотрите в файле redoc.yaml в директории /yatube_api/static/
или по следующему адресу:

```
http://127.0.0.1:8000/redoc/
```


## Автор:
Прудий Иван, ученик ЯндексПрактикум , курса Python-разработчик