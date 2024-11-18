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

Cмотрите в файле redoc.yaml в директории /yatube_api/static/
или по следующему адресу:

```
http://127.0.0.1:8000/redoc/
```