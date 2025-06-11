# Данный проект - это LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы

## Использование
В проекте доступно несколько вариантов использования
Инструкции к ним вы можете прочитать далее

## Использование с помощью docker-compose

1. Клонируйте репозиторий
```
git clone https://github.com/Daniil-Tarasov/LMS-systems.git
```

2. Поскольку проект использует Docker, необходимо установить [Docker](https://www.docker.com/products/docker-desktop/)
3. Откройте скопированный проект.
4. Переименуйте файл '.env.smple' в '.env' и внесите необходимые данные переменных окружения
5. Запустите проект командой: ```docker-compose up -d --build```
6. Для остановки всех контейнеров и их удаления используйте команду ```docker-compose down```

## Использование на удалённом сервере с docker-compose
### Настройка сервера

1. Откройте терминал и выполните команду для обновления списка пакетов на сервере: ```sudo apt update```
2. Затем выполните команду для обновления всех установленных пакетов до их последних версий: ```sudo apt upgrade```
3. Установите [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
4. Проверьте состояние файрвола с помощью команды: ```sudo ufw status``` и если фаервол отключен, активируйте его: ```sudo ufw enable```
5. Откройте необходимые порты: ```sudo ufw allow 80/tcp``` ```sudo ufw allow 443/tcp``` ```sudo ufw allow 22/tcp```

### Установка Git
1. Откройте терминал на сервере и выполните команду: ```sudo apt update``` ```sudo apt install git```
2. Клонируйте репозиторий:
```
git clone https://github.com/Daniil-Tarasov/LMS-systems.git
```

### Запуск
1. Перейдите в директорию, где находится файл docker-compose.yml: ```cd /your/path/LMS-systems```
2. Создайте файл .env и внесите необходимые переменные окружения на примере '.env.smple': ```nano .env```
3. Запустите проект командой: ```docker-compose up -d```

## Использование проекта с автоматическим деплоем
В проекте настроен файл GitHub Actions workflow(.github/workflows/ci.yaml).
Благодаря этому при каждом push проекта запускаются тесты и проект деплоится на удалённый сервер после успешного прохождения тестов.
Для корректной работы необходимо настроить секреты в вашем репозитории в GitHub.
1. Создайте секреты:
CELERY_BROKER_URL,
CELERY_BROKER_URL_FOR_TEST,
CELERY_RESULT_BACKEND,
CELERY_RESULT_BACKEND_FOR_TEST,
DATABASE_HOST,
DEPLOY_DIR,
DOCKER_HUB_ACCESS_TOKEN,
DOCKER_HUB_USERNAME,
EMAIL_HOST,
EMAIL_HOST_PASSWORD,
EMAIL_HOST_USER,
EMAIL_PORT,
EMAIL_USE_SSL,
EMAIL_USE_TLS,
POSTGRES_DB,
POSTGRES_PASSWORD,
POSTGRES_USER,
SECRET_KEY,
SERVER_IP,
SSH_KEY,
SSH_USER,
STRIPE_SECRET_KEY
2. В сервисах 'web', 'celery', 'celery-beat' в строке image укажите свой DOCKER_HUB_USERNAME

## Проверка работоспособности

1. Общая проверка:
   - Для общей проверки с использованием docker-compose можно воспользоваться командой ```docker-compose logs -f```. Если ошибок не выявлено можно считать проект работоспособным
   - Для проверки каждого из сервисов с использованием docker-compose можно использовать команду ```docker-compose logs <название сериса(например redis)>```
2. Проверка по отдельности:
    - Для проверки сервиса 'web' достаточно перейти на страницу сервера или выполнить запрос в Postman или другой программе
    - Для проверки сервиса 'db' можно ввести команду ```docker exec -it <db_container_id> psql -U <username>```. db_container_id можно получить командой ```docker ps```
    - Для проверки сервиса 'redis' введите команду ```docker-compose exec redis redis-cli ping```. Если в терминале получаем ответ 'PONG', значит сервис работает
    - Для проверки сервиса 'celery' введите команду ```docker-compose exec celery poetry run python manage.py shell -c "from users.tasks import check_last_login; check_last_login()"```
    - Для проверки сервиса 'celery-beat' достаточно проверить логи командой ```docker-compose logs celery-beat``` и убедиться, что beat scheduler запущен (-beat: Starting // -Scheduler: Sending due task...)