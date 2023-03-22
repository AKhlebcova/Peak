Peak API

ОБЗОР ЦЕЛЕЙ
Написание REST API, которая пользоляет пользователю вностить в имеющуюся БД сведения о перевалах:
1) координаты перевала и его высота;
2) имя пользователя;
3) почта и телефон пользователя;
4) название перевала;
5) несколько фотографий перевала.


МОДЕЛИ БД

1. Таблица с данными пользователей
```
Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
```
2. Таблица со сведениям о координатах и высотах перевалов
```
Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
```

3. Таблица содержащая фотографии и заголовки фотографий перевалов
```
Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}
```
4. Таблица со сведениям о перевалах
```
Add{
beauty_title	string
title: Beauty title
maxLength: 20
x-nullable: true
title*	string
title: Название
maxLength: 60
minLength: 1
other_titles	string
title: Дополнительное название
maxLength: 60
x-nullable: true
connect	string
title: Что соединяет (долины)
maxLength: 60
x-nullable: true
add_time*	string($date-time)
title: Дата регистрации
user*	Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
coords*	Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
level*	LevelSerialaizer{
winter	string
title: Категория трудности в зимний период
maxLength: 2
x-nullable: true
summer	string
title: Категория трудности в летний период
maxLength: 2
x-nullable: true
autumn	string
title: Категория трудности в осенний период
maxLength: 2
x-nullable: true
spring	string
title: Категория трудности в весенний период
maxLength: 2
x-nullable: true
 
}
images*	[Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}]
status	string
title: Status
readOnly: true
minLength: 1
 
}
```


МЕТОДЫ

GET
/submitData/


Возвращает описание всех добавленных перевалов

Parameters
Try it out
```Name	Description
user__email
string
(query)
```
Возвращает выборку перевалов, добавленных определенным пользователем по email


Responses
Response content type

Code	Description
200	
Example Value
```Model
[Add{
beauty_title	string
title: Beauty title
maxLength: 20
x-nullable: true
title*	string
title: Название
maxLength: 60
minLength: 1
other_titles	string
title: Дополнительное название
maxLength: 60
x-nullable: true
connect	string
title: Что соединяет (долины)
maxLength: 60
x-nullable: true
add_time*	string($date-time)
title: Дата регистрации
user*	Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
coords*	Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
level*	LevelSerialaizer{
winter	string
title: Категория трудности в зимний период
maxLength: 2
x-nullable: true
summer	string
title: Категория трудности в летний период
maxLength: 2
x-nullable: true
autumn	string
title: Категория трудности в осенний период
maxLength: 2
x-nullable: true
spring	string
title: Категория трудности в весенний период
maxLength: 2
x-nullable: true
 
}
images*	[Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}]
status	string
title: Status
readOnly: true
minLength: 1
 
}]
```

POST
/submitData/


Позволяет создавать новую запись о перевали с его подробным описанием

```
Add{
beauty_title	string
title: Beauty title
maxLength: 20
x-nullable: true
title*	string
title: Название
maxLength: 60
minLength: 1
other_titles	string
title: Дополнительное название
maxLength: 60
x-nullable: true
connect	string
title: Что соединяет (долины)
maxLength: 60
x-nullable: true
add_time*	string($date-time)
title: Дата регистрации
user*	Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
coords*	Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
level*	LevelSerialaizer{
winter	string
title: Категория трудности в зимний период
maxLength: 2
x-nullable: true
summer	string
title: Категория трудности в летний период
maxLength: 2
x-nullable: true
autumn	string
title: Категория трудности в осенний период
maxLength: 2
x-nullable: true
spring	string
title: Категория трудности в весенний период
maxLength: 2
x-nullable: true
 
}
images*	[Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}]
 
}
```
Responses
```
200	
Example Value
Model
{
status	integer
message	string
id	integer
 
}
```
```
400	
Example Value
Model
{
status	integer
message	string
id	integer
 
}
```
```
500	
Example Value
Model
{
status	integer
message	string
id	integer
 
}
```

GET
/submitData/{id}/


Возвращает всю информацию об объекте, в том числе статус модерации по её id

Parameters
Try it out
Name	Description
id *
integer
(path)
A unique integer value identifying this add.


Responses
Response content type

Code	Description
200	
Example Value
Model
```
Add{
beauty_title	string
title: Beauty title
maxLength: 20
x-nullable: true
title*	string
title: Название
maxLength: 60
minLength: 1
other_titles	string
title: Дополнительное название
maxLength: 60
x-nullable: true
connect	string
title: Что соединяет (долины)
maxLength: 60
x-nullable: true
add_time*	string($date-time)
title: Дата регистрации
user*	Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
coords*	Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
level*	LevelSerialaizer{
winter	string
title: Категория трудности в зимний период
maxLength: 2
x-nullable: true
summer	string
title: Категория трудности в летний период
maxLength: 2
x-nullable: true
autumn	string
title: Категория трудности в осенний период
maxLength: 2
x-nullable: true
spring	string
title: Категория трудности в весенний период
maxLength: 2
x-nullable: true
 
}
images*	[Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}]
status	string
title: Status
readOnly: true
minLength: 1
 
}
```
PATCH
/submitData/{id}/



Позволяет частично информацию о перевале в статусе newб кроме пользователя и статуса

```
data *
object
(body)
Example Value
Model
Add{
beauty_title	string
title: Beauty title
maxLength: 20
x-nullable: true
title*	string
title: Название
maxLength: 60
minLength: 1
other_titles	string
title: Дополнительное название
maxLength: 60
x-nullable: true
connect	string
title: Что соединяет (долины)
maxLength: 60
x-nullable: true
add_time*	string($date-time)
title: Дата регистрации
user*	Users{
email*	string($email)
title: E-mail
maxLength: 20
minLength: 1
fam*	string
title: Фамилия
maxLength: 20
minLength: 1
name*	string
title: Имя
maxLength: 20
minLength: 1
otc*	string
title: Отчество
maxLength: 20
minLength: 1
phone*	string
title: Номер телефона
maxLength: 25
minLength: 1
 
}
coords*	Coords{
latitude*	number
title: Широта
longitude*	number
title: Долгота
height*	integer
title: Высота
maximum: 2147483647
minimum: 0
 
}
level*	LevelSerialaizer{
winter	string
title: Категория трудности в зимний период
maxLength: 2
x-nullable: true
summer	string
title: Категория трудности в летний период
maxLength: 2
x-nullable: true
autumn	string
title: Категория трудности в осенний период
maxLength: 2
x-nullable: true
spring	string
title: Категория трудности в весенний период
maxLength: 2
x-nullable: true
 
}
images*	[Images{
data*	string
title: Data
title*	string
title: Название участка
maxLength: 30
minLength: 1
 
}]
 
}
id *
integer
(path)
A unique integer value identifying this add.
```

Responses

```
200	
Example Value
Model
{
state	integer
message	string
 
}
```
```
400	
Example Value
Model
{
state	integer
message	string
 
}
```


РАЗВОРАЧИВАНИЕ НА ХОСТИНГЕ

РАЗВЕРНУТ на хостинге по адресу http://158.160.28.162:8000/submitData/

1. Получение SSH ключа https://cloud.yandex.ru/docs/compute/operations/vm-connect/ssh и создание ВМ на яндекс облаке, получаем <имя> и <Публичный IPv4>
2. Устанавливаем соединение с ВМ командой в терминале  и <Публичный IPv4>
$ ssh <имя>@<Публичный IPv4>
3. Устанавливаем установщик пакетов pip:
$ sudo apt update
$ sudo apt install python3-venv python3-pip
$ sudo -H pip3 install --upgrade pip
4. Копируем из git-репозитория проект "Peak"
$ sudo apt install git
$ git clone https://github.com/AKhlebcova/Peak
5. Создаем виртуальное окружение:
$ python3 -m venv venv
6. Активируем виртуальное окружение:
$ cd Peak
$ source ../venv/bin/activate
7. Устанавливаем все пакеты:
$ pip install -r requirements.txt
8. Устанавливаем psql  и создаем db pereval, задаем пароль пользователя
$ sudo apt install postgresql postgresql-contrib
$ sudo -i -u postgres
$ psql
postgres=# createuser --interactive
postgres-# \q
postgres@python-venv:~$ createdb pereval
postgres=# \password postgres
Enter new password for user "postgres":
Enter it again:
postgres=# \q
postgres@python-venv:~$ exit
9. Производим миграции и создаем суперпользователя
$ python manage.py migrate
$ python manage.py createsuperuser

10. В файле settings.py редактируем:
ALLOWED_HOSTS = ['*']

11. Запускаем сервер:
$ python manage.py runserver 0.0.0.0:8000
12. Переходим по ссылке
http://<Публичный IPv4>/0.0.0.0:8000






