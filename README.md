# Auth DRF

Проект "Auth DRF" представляет собой пример приложения для регистрации пользователей и аутентификации с использованием токенов в Django REST Framework с использованием пакета Djoser.

Этот проект демонстрирует базовую реализацию системы регистрации пользователей, управления учетными записями и аутентификации через выдачу и проверку токенов, используя Djoser в Django REST Framework.

## Установка

1. Клонировать репозиторий:

    ```bash
    git clone git@github.com:AibekYrysbekov/Auth_DRF.git
    ```

2. Создать и активировать виртуальное окружение:

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # Для Linux/Mac
    .\myenv\Scripts\activate   # Для Windows
    ```

3. Установить зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создать файл `.env` в корне проекта и добавить туда конфиденциальные переменные окружения:

    ```
   EMAIL_HOST_USER = 'your_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_generated_app_password'
   DEFAULT_FROM_EMAIL = 'your_email@gmail.com'

    # Другие переменные
    ```

5. Запустить сервер:

    ```bash
    python manage.py runserver
    ```

6. Открыть браузер и перейти по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Настройки электронной почты

Для настройки отправки электронных писем необходимо указать параметры в файле `settings.py`:

      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_HOST = 'smtp.gmail.com'
      EMAIL_PORT = 587
      EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
      EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
      EMAIL_USE_TLS = True
      DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

Для безопасности рекомендуется использовать переменные окружения для хранения конфиденциальных данных.

## Документация API
Документация API доступна по следующим ссылкам:

Swagger UI: http://127.0.0.1:8000/swagger/
ReDoc: http://127.0.0.1:8000/redoc/

### Author: 
Aibek Yrysbekov
