# 1. Создаём виртуальное окружение:
   - python3 -m venv venv
   - source venv/bin/activate

# 2. Устанавливаем библиотеки:
   - pip install -r requirements.txt

# 3. Создаём БД через docker-compose:
   - docker-compose up -d

# 4. Запускаем DB + Приложени:
   - python3 models.py
   - python3 main.py



# Info: Данные БД:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=avito_aiohttp
      - PORTS: 5439

# Создаем запросы через файл (requests.http)
