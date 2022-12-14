# api_yamdb
### Описание

Это учебный проект для Яндекс.Практикума. С помошью него, кроме всего прочего отрабатывалась мое умени работать в команде с несколькими колобарантами

В данном проекте реализоавно API на основе Django REST framework. Данный програмный 
интерфейс позволяет выполнять взаимодействие с БД проекта Yamdb. Проект Yamdb представляет 
собой платформу для изучения инфоормации о произведениях искуства(кино, музыки и пр.) в различных 
жанрах и категориях, а также для оставления отзывов к этим произведениям. Аутентификация производится с помошью JWT-токена.

### Установка:

1) Запустите терминал и откройте в нем папку, в которую хотите клонировать проект.
2) Клонируйте репозиторий и перейдите в него в командной строке:

```
https://github.com/Spacemarine1789/api_final_yatube.git
```

```
cd api_final_yatube
```

3) Cоздате и активируйте виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Если вы пользователь **Windows**:

```
source env/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

4) Установите зависимости из файла **requirements.txt**:

```
pip install -r requirements.txt
```

5) Выполните миграции:

```
python3 manage.py makemigrations
python3 manage.py migrate
```
обратите внимание что запускать проект и выполнять миграции необходимо из дериктории, 
в которой расположен файл **manage.py**.

6) Запустите проект:

```
python3 manage.py runserver
```

# Ресурсы API YaMDb
**AUTH**: аутентификация.

**USERS**: пользователи.

**TITLES**: произведения.

**CATEGORIES**: категории произведений.

**GENRES**: жанры произведений.

**REVIEWS**: отзывы на произведения.

**COMMENTS**: комментарии к отзывам.

# Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

**Аутентифицированный пользователь (user)** — может читать всё, как и Аноним, дополнительно может публиковать отзывы и ставить оценки произведениям, может комментировать чужие отзывы, может редактировать и удалять свои отзывы и комментарии.

**Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя, а так же право удалять и редактировать любые отзывы и комментарии.

**Администратор (admin)** — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

**Администратор Django** — те же права, что и у роли Администратор.

# ReDoc
Подробности об этом API, а так же примеры запросов можно найти в ReDoc документации по адресу:
```
/redoc/
```
