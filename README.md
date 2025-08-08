Для запуска проекта требуется Python >= 3.9

- Docker
- Docker Compose
- Файл `.env` с переменными окружения (пример в `.env.example`)

## Шаги развёртывания

### 1. Клонируем репозиторий

```bash
git clone https://github.com/Artem468/richat_test.git
```

### 2. Заходим в каталог

```bash
cd richat_test
```

### 3. Создаём файл .env и заполняем его

```bash
cp .env.example .env
```

### 4. Собираем и запускаем docker контейнер

```bash
docker-compose build
docker-compose up -d
```

### 5. Создаем БД, выполняем миграции и создаём суперпользователя

```bash
docker-compose exec db psql -U postgres
CREATE DATABASE db_name;
exit                
```

```bash
docker-compose exec web sh
python manage.py migrate
python manage.py createsuperuser
exit
```