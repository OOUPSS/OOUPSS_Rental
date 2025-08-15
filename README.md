# 🚀 OOUPSS_Rental — Next-Gen Housing Rental Backend API 🏠

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django REST](https://img.shields.io/badge/Django%20REST-Framework-green?logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple?logo=open-source-initiative)
![Status](https://img.shields.io/badge/Status-Active-success)
![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?logo=github)

**OOUPSS_Rental** — the ultimate backend for a modern rental service. Powerful, secure, and scalable.  
Built with **Django REST Framework**, crafted with love for code and architecture. 💎

---

## ✨ Features

| 🚀 Feature | 📜 Description |
|------------|----------------|
| 🏠 **Property Management** | Full CRUD for adding, editing, and deleting listings. |
| 🔐 **Authentication & Roles** | Secure registration and login. Roles: **Landlord** and **Tenant**. |
| 🔍 **Search & Filtering** | Keyword search + filtering by price, rooms, and location. |
| 📅 **Booking Lifecycle** | Complete booking cycle: creation, approval, cancellation, rejection. |
| ⭐ **Reviews & Ratings** | Leave reviews and ratings only after a completed rental. |
| 📚 **Swagger UI** | Auto-generated interactive documentation for API testing. |

---

## 🛠️ Installation (Local)

### 📋 Prerequisites
- Python **3.11** 🐍
- pip 📦
- MySQL Server 🗄️

### 1️⃣ Clone the project
```bash
git clone <YOUR_REPOSITORY_URL>
cd ooupss_rental

# OOUPSS Rental

This is the setup guide for the Ooupss Rental project, a Django-based application. Follow the steps below to set up and run the project locally.

## Setup Instructions

### 1️⃣ Clone the Project
Clone the repository and navigate to the project directory:
```bash
git clone <YOUR_REPOSITORY_URL>
cd ooupss_rental
```

### 2️⃣ Create a Virtual Environment
Set up a Python virtual environment to isolate project dependencies:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the Database
Create a `.env` file in the root of the project and add the following environment variables:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5️⃣ Apply Migrations
Run the database migrations to set up the database schema:
```bash
python manage.py migrate
```

### 6️⃣ Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

📍 The API will be available at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📚 API Documentation
Explore and test the API endpoints interactively using Swagger UI:  
[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## 👥 Development Team
- **OOUPSStech** — Full-Stack Developer 🛠️
  Building and maintaining the core of the project.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
