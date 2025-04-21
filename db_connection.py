import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="bookstore-db.c98oekou8pt9.us-east-2.rds.amazonaws.com",
            user="admin",
            password="Sweta2560",
            database="bookstore"
        )
        if connection.is_connected():
            print("Connected to the database!")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

def create_tables():
    """
    Drops and creates the required tables for the application.
    Ensures referential integrity with proper constraints and cascading behavior.
    """
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to the database. Exiting...")
        return
    
    cursor = connection.cursor()

    try:
        # Drop existing tables (if any)
        cursor.execute("DROP TABLE IF EXISTS orders;")
        cursor.execute("DROP TABLE IF EXISTS customers;")
        cursor.execute("DROP TABLE IF EXISTS books;")
        cursor.execute("DROP TABLE IF EXISTS authors;")

        # Create `authors` table
        cursor.execute("""
            CREATE TABLE authors (
                author_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL
            )
        """)

        # Create `books` table
        cursor.execute("""
            CREATE TABLE books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author_id INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
                stock INT NOT NULL CHECK (stock >= 0),
                CONSTRAINT fk_author FOREIGN KEY (author_id) 
                    REFERENCES authors(author_id)
                    ON DELETE CASCADE
            )
        """)

        # Create `customers` table
        cursor.execute("""
            CREATE TABLE customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                phone VARCHAR(20)
            )
        """)

        # Create `orders` table
        cursor.execute("""
            CREATE TABLE orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                book_id INT NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0),
                CONSTRAINT fk_customer FOREIGN KEY (customer_id) 
                    REFERENCES customers(customer_id)
                    ON DELETE CASCADE,
                CONSTRAINT fk_book FOREIGN KEY (book_id) 
                    REFERENCES books(book_id)
                    ON DELETE CASCADE
            )
        """)

        cursor.execute("""
        CREATE TABLE order_details (
            order_detail_id SERIAL PRIMARY KEY,
            order_id INT REFERENCES orders(order_id),
            book_id INT REFERENCES books(book_id),
            quantity INT NOT NULL
            )
        """)

        connection.commit()
        print("Tables created successfully!")

    except Error as err:
        print(f"Error while creating tables: {err}")
    finally:
        cursor.close()
        connection.close()
        print("Database connection closed.")

# Test database connection and table creation
if __name__ == "__main__":
    create_tables()
