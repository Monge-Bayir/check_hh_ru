# ETL-пайплайн для анализа вакансий с HeadHunter
 Проект представляет собой ETL-пайплайн на Python, который собирает данные о вакансиях с API HeadHunter, обрабатывает их и сохраняет в базу данных PostgreSQL.

## 🚀 Возможности

✅ Сбор данных через API HeadHunter

✅ Очистка и трансформация данных (обработка зарплат, дат и т.д.)

✅ Сохранение в CSV и PostgreSQL

✅ Автоматическое создание таблиц в БД

✅ Резервное сохранение при ошибках

## ⚙️ Установка и настройка
1. Требования
```
Python 3.9+

PostgreSQL (если используется)

Библиотеки: pandas, requests, sqlalchemy, psycopg2-binary
```
2. Установка зависимостей
```bash
pip install -r requirements.txt
```

3. Настройка БД (опционально)
Создайте файл config/settings.py с настройками подключения:

```python
DB_CONFIG = {
    "USER": "ваш_пользователь",
    "PASS": "ваш_пароль",
    "HOST": "localhost",
    "NAME": "название_бд"
}
```
## 🚀 Запуск
Основной ETL-пайплайн

```bash
python scripts/main.py
```

### Отдельные этапы

Извлечение данных:
```bash
python scripts/extract.py
```

Очистка данных:

```bash
python scripts/transform.py
```
Загрузка в БД:

```bash
python scripts/load.py
```
## 📂 Структура проекта
```text
check_hh_ru/
├── data/                    # Данные (сырые и обработанные)
│   ├── refined/                 
│   └── unrefined/          
├── scripts/                 # Основные скрипты
│   ├── extract.py           # Загрузка данных с HH API
│   ├── transform.py         # Очистка данных
│   ├── load.py              # Сохранение в CSV/PostgreSQL
│   └── main.py              # Главный пайплайн
├── config/                  # Конфигурации
│   └── settings.py          # Настройки БД
├── tests/                   # Тесты
├── requirements.txt         # Зависимости
└── README.md                # Документация
```
## 🔧 Технологии
Python (Pandas, Requests, SQLAlchemy)

PostgreSQL (хранение данных)

ETL-методология (Extract, Transform, Load)

## 📌 Дальнейшее развитие
🔹 Добавить Airflow для автоматизации

🔹 Реализовать веб-интерфейс (Dash/Streamlit)

🔹 Добавить аналитику (средние зарплаты, топ-навыков)
