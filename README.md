# 📚 Online Bookstore – Cloud Computing Project

This project is a **cloud-ready online bookstore system** developed using **PHP** and **MySQL**, designed as part of the course **COSC5756002 - Cloud Computing**. It demonstrates core backend service architecture, dynamic content rendering, database integration, and web-based user interaction.

---

## 🎯 Project Overview

The **Online Bookstore** simulates a functional e-commerce platform where users can register, browse books, add them to a cart, and place orders. Admins can manage inventory and orders. Though currently hosted locally, the project is structured for deployment to cloud platforms (like AWS, Heroku, etc.).

---

## ✨ Features

### 🔐 User Authentication
- Register/Login system
- Session-based access control

### 📘 Book Management
- View all books with search filters
- Admin: Add, Edit, Delete books and categories

### 🛒 Shopping Cart
- Add/remove books from cart
- Simulate checkout process

### 📦 Orders
- Users can view order history
- Simulated order management

### 🧑‍💼 Admin Dashboard
- User, Book, Category, and Order management
- Overview dashboard for quick stats

---

## 📂 Project Structure

```
online_bookstore/
│
├── admin/               # Admin portal pages
├── assets/              # CSS, JS, and images
├── includes/            # Shared components: DB, header/footer
├── user/                # Login, register, user profile, cart
├── index.php            # Homepage
├── book_details.php     # View single book
├── browse.php           # Browse books by category
└── bookstore.sql        # MySQL DB schema
```

---

## ⚙️ Setup Instructions

### 🗃️ 1. Clone the Repository

```bash
git clone https://github.com/your-username/online_bookstore.git
```

Or [download the ZIP](https://github.com/your-username/online_bookstore/archive/refs/heads/main.zip) and extract it into your server directory.

---

### 🛠️ 2. Import the Database

- Open **phpMyAdmin** or use **MySQL CLI**
- Import the file `bookstore.sql`

```bash
mysql -u root -p < bookstore.sql
```

---

### 🔧 3. Configure Database Connection

Edit the file `includes/db.php` to match your local DB credentials:

```php
$host = 'localhost';
$user = 'root';
$pass = '';        // your DB password
$dbname = 'bookstore';
```

---

### 🚀 4. Run the App

- Move the project folder to `htdocs/` if using **XAMPP**
- Start **Apache** and **MySQL** from XAMPP Control Panel
- Open your browser and go to:

```
http://localhost/online_bookstore/
```

✅ You should now see the bookstore homepage!

---


## 🌐 Cloud Deployment (Future Scope)

Though currently hosted locally, this project can be deployed on:
- **Heroku** using PHP buildpack
- **AWS Lightsail / EC2** with LAMP stack
- **cPanel** based shared hosting

For deployment help, refer to the [deployment guide](#).

---

## 💡 Future Enhancements

- 📱 Responsive UI using Bootstrap 5
- 💳 Payment gateway integration (Razorpay/Stripe)
- 📝 User reviews and star ratings for books
- 📊 Admin dashboard with analytics
- 📦 Email/SMS notifications for orders

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to suggest changes, please fork the repo and submit a pull request.

