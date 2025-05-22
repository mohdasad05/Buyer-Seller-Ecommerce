# Sabhyasha E-commerce Backend

A basic e-commerce backend system built using Django, Django REST Framework, MySQL, and JWT authentication.

## 🚀 Features

- Custom user registration with buyer/seller roles
- JWT authentication using SimpleJWT
- Product CRUD for sellers
- Product listing with pagination & filtering
- Buyers can place orders with multiple items
- Role-based order views
- Admin panel to manage users, products, and orders
- MySQL database support via XAMPP/phpMyAdmin
- Postman collection available for API testing
- Database dump included for easy setup

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- MySQL (MariaDB via XAMPP)
- JWT Authentication (SimpleJWT)
- Postman

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mohdasad05/sabhyasha-ecommerce.git
cd sabhyasha-ecommerce
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the MySQL Database

- Open **XAMPP Control Panel**
- Start **Apache** and **MySQL**
- Go to [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
- Create a new database named: `sabhyasha_db`

### 6. Import the SQL Dump (instead of migrations)

- In phpMyAdmin, click the `sabhyasha_db` database
- Go to the **Import** tab
- Click **Choose File** and select `sabhyasha_ecommerce.sql` from the repo
- Click **Go**

✅ This will import all required tables and data.

### 7. Update `.env` File

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
DB_NAME=sabhyasha_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 API Access & Testing

You can test the API endpoints using:
- Swagger or ReDoc (if enabled)
- Postman (a collection file is provided in the repo)

---

## 🗃 Database Dump

- The file `sabhyasha_ecommerce.sql` is provided in the repository
- You can import it directly via phpMyAdmin to skip migrations

---

## 📂 Project Structure

```
sabhyasha-ecommerce/
│
├── accounts/                   # CustomUser model & registration APIs
├── products/                   # Product models & views
├── orders/                     # Order & OrderItem models
├── sabhyasha_ecommerce/        # Project settings
├── requirements.txt            # Dependencies
├── .env                        # Environment config (you create it)
├── sabhyasha_ecommerce.sql     # MySQL database dump
├── README.md
└── manage.py
```

---

## 📦 License

© 2025 Sabhyasha Retail Tech Pvt. Ltd. – All rights reserved.
