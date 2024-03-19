# Проект "Онлайн Кинотеатр"

Репозиторий для UGC (User-Generated Content) сервиса, который позволяет пользователям создавать различные действия и контент. Этот сервис является частью проекта "Онлайн Кинотеатр" и состоит из двух частей: ugc_api, отвечающего за сохранение действий пользователя в kafka, и ugc_etl, который передает данные из Kafka в ClickHouse для последующего анализа.

## Содержание:

- [Django Admin Panel](https://github.com/kaedeMirai/new_admin_panel_sprint_1)
- [ETL from Postgresql to Elastic](https://github.com/kaedeMirai/admin_panel_sprint_3)
- [Auth](https://github.com/kaedeMirai/Auth_sprint_1-2)
- [UGC](https://github.com/kaedeMirai/ugc_sprint_1)
- [UGC +](https://github.com/kaedeMirai/ugc_sprint_1)
- [Notification service]()
- [Watch Together service]()

## Где найти код?
1. [ugc api + ugc etl](https://github.com/kaedeMirai/ugc_sprint_1) - здесь хранится код ugc api и ugc etl

## Ссылка на документацию api
1. http://0.0.0.0:80/api/openapi

## Инструкция по запуску проекта
1. Склонировать репозиторий

   ```
   git clone https://github.com/kaedeMirai/ugc_sprint_1.git
   ```
2. Скопировать .env.example в .env (либо переименовать .env.example) и заполнить их (в папках ugc_api и ugc_etl)
4. В командной строке запустить проект (сначала запускается etl)

    ```
    cd ugc_etl
    make build_image
    make run_dev

    cd ..
    cd ugc_api
    make build image
    make run_prod_like
    ```
