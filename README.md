# Проектная работа 8 спринта

## Где найти код?
1. [ugc api + ugc etl](https://github.com/Munewxar/ugc_sprint_1) - здесь хранится код ugc api и ugc etl

## Ссылка на документацию api
1. http://0.0.0.0:80/api/openapi

## Инструкция по запуску проекта
1. Склонировать репозиторий

   ```
   git clone https://github.com/Munewxar/ugc_sprint_1.git
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
