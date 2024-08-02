[UA](#сайт-каталог-керамічних-виробів) / [EN](#ceramics-catalog-website)

# Сайт каталог керамічних виробів
Це проект сайту каталогу керамічних виробів, створений за допомогою Django для учбових цілей

## Вміст
- [Особливості](#особливості)
- [Вимоги](#вимоги)
- [Установка](#установка)
- [Використання](#використання)
- [Структура Проекту](#структура-проекту)

## Особливості
- **Каталог продуктів**: Створення, редагування, видалення розділів, підрозділів та виробів з детальною інформацією.
- **Адміністративна панель**: Управління продуктами, категоріями та іншими даними.
- **Фронтенд**: Створено з використанням Bootstrap 5 для адаптивного дизайну.
- **Імпорт-Експорт**: Можливість імпортувати, в каталог, CSV файлу зі списком товарів та експорту CSV для подальшого створення прайсу.
  
## Вимоги
- Python 3.x
- Django 3.x
- SQLite (за замовчуванням)

## Установка
1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/MicZoloto/ceramica_site.git
   cd ceramica_site
   ```
   
2. Створіть віртуальне середовище та активуйте його:
   ```bash
   python -m venv venv
   source venv/bin/activate   # на Windows: venv\Scripts\activate
   ```
   
3. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Застосуйте міграції:
   ```bash
   python manage.py migrate
   ```

## Використання
1. Запустіть сервер розробки:   
   ```bash
   python manage.py runserver
   ```
2. Відвідайте сайт за адресою http://127.0.0.1:8000/

## Структура Проекту
- **ceramica/**: Головна папка проекту Django.
- **templates/**: HTML шаблони для рендерингу сторінок.
- **static/**: Статичні файли (CSS, JS, зображення).
- **manage.py**: Командний скрипт Django.
  
## Ліцензія
Цей проект ліцензований під **MIT License**.

***
***

# Ceramics Catalog Website
This is a project of a ceramics catalog website created using Django for educational purposes.

## Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features
- **Product Catalog**: Create, edit, delete sections, subsections, and products with detailed information.
- **Admin Panel**: Manage products, categories, and other data.
- **Frontend**: Built using Bootstrap 5 for responsive design.
- **Import-Export**: Import CSV files with product lists into the catalog and export CSV for price list creation.

## Requirements
- Python 3.x
- Django 3.x
- SQLite (default)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MicZoloto/ceramica_site.git
   cd ceramica_site
   ```
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Usage
1. Run the development server:   
   ```bash
   python manage.py runserver
   ```
2. Visit the site at http://127.0.0.1:8000/

## Project Structure
- **ceramica/**: Main Django project folder.
- **templates/**: HTML templates for rendering pages.
- **static/**: Static files (CSS, JS, images).
- **manage.py** : Django command script.

## License
This project is licensed under the **MIT License**.
