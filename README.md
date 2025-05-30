# Данный проект - это LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы

## Установка

1. Клонируйте репозиторий
```
git clone https://github.com/Daniil-Tarasov/LMS-systems.git
```

2. Поскольку проект использует Docker, необходимо установить [Docker](https://www.docker.com/products/docker-desktop/)

## Использование

1. Откройте скопированный проект.
2. Переименуйте файл '.env.smple' в '.env' и внесите необходимые данные переменных окружения
3. Запустите проект командой: ```docker-compose up -d --build```
4. Для остановки всех контейнеров и их удаления используйте команду ```docker-compose down```

## Проверка работоспособности

1. Общая проверка:
   - Для общей проверки можно воспользоваться командой ```docker-compose logs -f```. Если ошибок не выявлено можно считать проект работоспособным
   - Для проверки каждого из сервисов можно использовать команду ```docker-compose logs <название сериса(например redis)>```
2. Проверка по отдельности:
    - Для проверки сервиса 'web' достаточно перейти на страницу http://localhost:8000 или выполнить запрос в Postman или другой программе
    - Для проверки сервиса 'db' можно ввести команду ```docker exec -it <db_container_id> psql -U <username>```. db_container_id можно получить командой ```docker ps```
    - Для проверки сервиса 'redis' введите команду ```docker-compose exec redis redis-cli ping```. Если в терминале получаем ответ 'PONG', значит сервис работает
    - Для проверки сервиса 'celery' введите команду ```docker-compose exec celery poetry run python manage.py shell -c "from users.tasks import check_last_login; check_last_login()"```
    - Для проверки сервиса 'celery-beat' достаточно проверить логи командой ```docker-compose logs celery-beat``` и убедиться, что beat scheduler запущен (-beat: Starting // -Scheduler: Sending due task...)