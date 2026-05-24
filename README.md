# 🍽️ eDine-In — Restaurant Management And Online Food Ordering System

A full-stack food ordering platform built using **Python and Django (MVT Architecture)** that streamlines restaurant operations and delivers a seamless online food ordering experience.

The application enables customers to browse menus, manage carts, place orders, and track order progress in real time, while administrators can efficiently manage food items, categories, and customer orders through a centralized dashboard.

The project also implements secure authentication workflows including **OTP-based email verification, password recovery, and session management** to enhance user security and experience.

---

# 📖 Overview

eDine-In is a backend-focused web application designed to simplify restaurant operations through digital order management and user-friendly food ordering workflows.

The platform provides:

* Secure user authentication
* Dynamic food menu browsing
* Cart and checkout functionality
* Real-time order status tracking
* Administrative control over restaurant operations

The project follows Django’s **Model–View–Template (MVT)** architecture for clean code organization, scalability, and maintainability.

---

# ✨ Key Highlights

* Built using Django MVT architecture
* Secure OTP-based email authentication system
* Real-time order lifecycle tracking
* Session-based cart management
* Normalized relational database design
* Password recovery & account security workflows
* Modular backend structure
* Dynamic categorized food menu system
* Scalable and maintainable code organization

---

# 🚀 Features

## 🔐 Authentication & Security

* User registration and login system
* Email OTP verification for account activation
* Secure login and logout functionality
* Forgot password with OTP verification
* Password reset functionality
* Change password option for authenticated users
* Session-based authentication and management
* Form validation and protected routes

---

## 🍔 Food Ordering System

* Dynamic categorized menu browsing
* Food item listing with images and pricing
* Add to cart functionality
* Update cart quantities
* Remove items from cart
* Checkout and order placement workflow
* Real-time order status tracking
* Order summary generation

---

## 🛠️ Admin Functionalities

* Food item management
* Category management
* Order management dashboard
* Order status updates
* Customer order monitoring

---

## 🗄️ Database & Backend

* Normalized relational database schema
* Django ORM integration
* Modular backend architecture
* Efficient database relationships
* Scalable data model structure

---

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django ORM

## Frontend

* HTML5
* CSS3
* JavaScript

## Database

* SQLite

## Authentication & Security

* Email OTP Verification
* Session Authentication

## Architecture

* Django MVT (Model–View–Template)

## Tools & Utilities

* Pillow (Image Handling)
* Git & GitHub

---

# 🏗️ Project Architecture

The application follows Django’s **MVT (Model–View–Template)** architecture:

* **Models** handle database structure and relationships
* **Views** process business logic and request handling
* **Templates** render dynamic UI content

This separation improves:

* Scalability
* Maintainability
* Code organization
* Development efficiency

---

# 🧠 System Workflow

1️⃣ User Registration & OTP Verification
2️⃣ Secure Login Authentication
3️⃣ Dynamic Menu Browsing
4️⃣ Cart Operations (Add / Update / Remove)
5️⃣ Checkout & Order Placement
6️⃣ Real-Time Order Status Tracking
7️⃣ Password Management (Forgot / Reset / Change Password)
8️⃣ Admin Dashboard Operations

---

# 🗄️ Database Design

The project uses **Django ORM** with normalized relational models to ensure efficient querying and data integrity.

## Core Models

* Users
* Categories
* Food Items
* Cart
* Cart Items
* Orders
* Order Status

## Database Design Goals

* Reduce data redundancy
* Maintain relational consistency
* Support scalable order workflows
* Improve query performance
* Maintain data integrity

---

# 🔒 Security Features

* OTP-based email verification
* Secure password reset workflow
* Session-based authentication
* CSRF protection using Django middleware
* Form validation and input sanitization
* Protected authenticated routes

---

# ⚙️ Installation & Setup

## Prerequisites

* Python 3.x
* Django
* Virtual Environment (Recommended)
* Pillow Library

---

## Clone the Repository

```bash
git clone https://github.com/beheradeeptimayee/Restaurant-Management-And-Online-Food-Ordering-System.git
```

---

## Navigate to Project Directory

```bash
cd Restaurant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

---

## Open in Browser

```bash
http://127.0.0.1:8000/
```

---

# 📂 Project Structure

```b
Restuarant/
│
├── accounts/
├── menu/
├── orders/
├── cart/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

* Django backend development
* Authentication workflows
* OTP verification systems
* Relational database design
* Session and user management
* CRUD operations
* Backend architecture design
* Full stack web integration
* Scalable project structuring

---

# 🚀 Future Enhancements

* Online payment gateway integration
* Real-time order notifications
* Restaurant analytics dashboard
* Mobile responsive UI redesign
* REST API integration using Django REST Framework
* JWT Authentication
* Docker-based deployment
* Cloud deployment support
* AI-based food recommendations

# 📄 License

This project is developed for educational and portfolio purposes.
