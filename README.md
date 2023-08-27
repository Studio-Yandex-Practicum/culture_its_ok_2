# Бот АНО "Культура”

![culture_its_ok_2 workflow](https://github.com/Studio-Yandex-Practicum-Hackathons/culture_its_ok_2/actions/workflows/culture_its_ok_2.yml/badge.svg)

## Описание
Бот проводит экскурсию-медитацию по местам г. Ростова с работами уличных художников.

## Подготовка к использованию бота
### Склонируйте репозиторий на локальную машину:
```
git clone https://github.com/Studio-Yandex-Practicum-Hackathons/culture_its_ok_2.git
```
* В файле settings.py впишите свой IP в следующей строчке: CSRF_TRUSTED_ORIGINS = ['http://your_ip_adress']
* Локально отредактируйте файл infra/nginx/default.conf и в строке server_name впишите свой IP
* В корне проекта создайте .env файл по аналогии с файлом .env.example:
    ```
    TELEGRAM_TOKEN="telegram_token_ID"
    SECRET_KEY="secret_key_django"
    ADMIN_ID="id телеграма администратора бота"
    SPREADSHEET_ID="spreadsheet_id"
    TYPE="type"
    PROJECT_ID="project_id"
    PRIVATE_KEY_ID="private_key_id"
    PRIVATE_KEY="private_key"
    CLIENT_EMAIL="client_email"
    CLIENT_ID="client_id"
    AUTH_URI="auth_uri"
    TOKEN_URI="token_uri"
    AUTH_PROVIDER_X509_CERT_URL="auth_provider_x509_cert_url"
    CLIENT_X509_CERT_URL="client_x509_cert_url"
    DB_ENGINE= "django.db.backends.postgresql"
    DB_NAME="имя базы данных postgres"
    POSTGRES_USER="пользователь бд"
    POSTGRES_PASSWORD="пароль"
    DB_HOST="db"
    DB_PORT="5432"
    URL_TABLE_FEEDBACK = "Cсылка_на_таблицу_опросов"
    ```

## Запуск проекта на удаленном сервере

* Установите docker на сервер:
```
sudo apt install docker.io
```
* Установите docker-compose на сервер:
```
sudo apt install docker-compose
```

* Скопируйте папку infra и файл .env на сервер:
```
scp -r /infra <username>@<host>:/home/<username>/
scp .env <username>@<host>:/home/<username>/
```
* На сервере соберите контейнеры:
```
sudo docker-compose up -d --build
```
* После сборки контейнеров на сервере выполните команды (только после первого деплоя):
    - Примените миграции:
    ```
    sudo docker-compose exec web python manage.py migrate
    ```
    - Создайте суперпользователя Django:
    ```
    sudo docker-compose exec web python manage.py createsuperuser
    ```
    - Соберите статику:
    ```
    sudo docker-compose exec web python manage.py collectstatic --noinput
    ```

* Для заполнения или обновления базы данных по маршрутам и экспонатам, а также для выгрузки отчётов в pdf перейдите по адресу https://your_ip_adress/admin
* Бот готов к работе.
* Перейдите в телеграм и следуйте инструкциям бота.
* Приятной экскурсии!

## Используемые технологии

- [![Python](https://img.shields.io/badge/-Python_3.11-464646?style=flat-square&logo=Python)](https://www.python.org/)
- [![Django](https://img.shields.io/badge/-Django_4.1-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
- [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
- [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
- [![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
- [![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
- [![Aiogram](https://img.shields.io/badge/Aiogram-3.0.0rc1-green?logo=Aiogram&logoColor=green)](https://aiogram.dev/)
- [![reportlab](https://img.shields.io/badge/reportlab-4.0.4-green?logo=reportlab&logoColor=green)](https://pypi.org/project/reportlab/)
- [![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10-green?logo=django_ckeditor&logoColor=green)](https://pypi.org/project/SpeechRecognition/)
- [![django_ckeditor](https://img.shields.io/badge/django_ckeditor-6.7.0-green?logo=django_ckeditor&logoColor=green)](https://pypi.org/project/django-ckeditor/)
- [![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

## Авторы:

**Изимов Арсений**  - студент Яндекс.Практикума Когорта 16+
https://github.com/Arseny13

**Дмитрий Абрамов**  - студент Яндекс.Практикума Когорта 16+
https://github.com/D-Abramoc/

**Вадим Конюшков**  - студент Яндекс.Практикума Когорта 16+
https://github.com/Vadikray

**Алексей Боборыкин**  - студент Яндекс.Практикума Когорта 16+
https://github.com/alexey-boborykin

**Роман Пекарев**  - студент Яндекс.Практикума Когорта 16+
https://github.com/ropek745

**Баранов Виктор**  - студент Яндекс.Практикума Когорта 16+
https://github.com/vityn101979