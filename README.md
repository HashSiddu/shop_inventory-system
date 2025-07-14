# shop_inventory-system

# 🛒 Shop Inventory – Django App

A clean and responsive **Django + Bootstrap** web app to manage shop inventory.  
Add, update, delete, and search products with real-time stock tracking.

## 🔧 Features
- Add/edit/delete items with category and price
- Track stock status (In stock / Low / Out of stock)
- Search and filter items quickly
- Admin panel for inventory management
- Mobile-friendly UI with Bootstrap 5 + Google Fonts

## 🛠 Tech Stack
- Django 5
- Bootstrap 5
- SQLite (dev)
- HTML + Django Templates




cd shop-inventory
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



📁 Project Structure

inventory/ – App with models, views, templates
templates/inventory/ – HTML pages (home, list, form)
shop_inventory/ – Django project config
