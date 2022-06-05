# Test FastAPI+sqlalchemy+asyncpg

## Деплой на локальную машину

#### Необходимо установить Redis
Ссылка на установку https://redis.io/docs/getting-started/installation/
#### Деплой
Клонируйте репозиторий:
```commandline
$ https://github.com/leondav1/FastAPI-sqlalchemy-asyncpg.git
$ cd FastAPI-sqlalchemy-asyncpg
```
Создайте виртуальную среду для установки зависимостей и активируйте ее:
```commandline
$ python -m venv env
$ source env/bin/activate
```
Затем установите зависимости:
```commandline
(env)$ pip install -r requirements.txt
```
#### Теперь необходимо настроить базу данных PostgreSQL.
Установите базу данных PostgreSQL, если её у вас ещё нет.
1. Откройте консоль PostgreSQL
```commandline
sudo -u postgres psql postgres
```
2. Затем задайте пароль администратора БД
```db2
\password postgres
```
3. Далее необходимо создать и настроить пользователя, при помощи которого будем соединяться с БД. Ну и также укажем значения по умолчанию для кодировки, уровня изоляции транзакции и временного пояса
```db2
create user <имя пользователя> with password '<пароль>';
alter role <имя пользователя> set client_encoding to 'utf8';
alter role <имя пользователя> set default_transaction_isolation to 'read committed';
alter role <имя пользователя> set timezone to 'UTC';
```
Временной поям можете указать свой, согласно файла settings.py.
4. Создайте базу для проекта и выйти из консоли
```db2
create database <имя БД> owner <имя пользователя>;
\q
```
5. В командной строке создайте файл .env, подставив в строку свои значения:
```commandline
echo DATABASE_URL=postgresql+asyncpg://user_name:password@host_name:5432/name_db > .env
```
Запускаем сервер:
```commandline
uvicorn main:app --reload
```
Страница доступна по адресу: http://127.0.0.1:8000/docs
