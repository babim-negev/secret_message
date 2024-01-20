One Babim Secret

One Babim Secret - это веб-приложение, которое позволяет создавать секретные ссылки, доступные только один раз.
Функционал:
    Создание секретной ссылки
        Генерация случайного URL
        Шифрование сообщения
        Сохранение в БД: секретное сообщение, ссылка, счетчик просмотров
    Открытие ссылки
        Проверка наличия в БД
        Проверка счетчика просмотров
        Дешифровка и вывод сообщения
        Увеличение счетчика просмотров
    Удаление ссылки по таймауту

Стек

    FastAPI
    Postgres
    Криптография: AES, хеширование


Запуск

Copy code
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload