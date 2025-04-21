from db_connection import connect_to_database

# Helper function for executing queries
def execute_query(query, params=None, fetchone=False, fetchall=False, dictionary=False):
    """
    Executes a given query with optional parameters.
    Handles connection management automatically.

    :param query: SQL query string
    :param params: Parameters for the query
    :param fetchone: Whether to fetch a single result
    :param fetchall: Whether to fetch all results
    :param dictionary: Whether to return results as dictionaries
    :return: Query results if fetchone or fetchall is True, else None
    """
    connection = connect_to_database()
    if not connection:
        raise Exception("Failed to connect to the database.")
    
    cursor = connection.cursor(dictionary=dictionary)
    try:
        cursor.execute(query, params)
        if fetchone:
            return cursor.fetchone()
        if fetchall:
            return cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()
        connection.close()


# CRUD for Books
def add_book(title, author_id, price, stock):
    execute_query(
        "INSERT INTO books (title, author_id, price, stock) VALUES (%s, %s, %s, %s)",
        (title, author_id, price, stock)
    )

def get_books_in_stock():
    return execute_query(
        "SELECT book_id, title, price, stock FROM books WHERE stock > 0",
        fetchall=True, dictionary=True
    )

def update_book(book_id, title, price, stock):
    execute_query(
        """
        UPDATE books
        SET title = %s, price = %s, stock = %s
        WHERE book_id = %s
        """,
        (title, price, stock, book_id)
    )

def delete_book(book_id):
    execute_query("DELETE FROM books WHERE book_id = %s", (book_id,))


# CRUD for Customers
def add_customer(first_name, last_name, email, phone):
    execute_query(
        "INSERT INTO customers (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, phone)
    )

def get_customers():
    return execute_query(
        "SELECT customer_id, first_name, last_name, email, phone FROM customers",
        fetchall=True, dictionary=True
    )

def update_customer(customer_id, first_name, last_name, email, phone):
    execute_query(
        """
        UPDATE customers
        SET first_name = %s, last_name = %s, email = %s, phone = %s
        WHERE customer_id = %s
        """,
        (first_name, last_name, email, phone, customer_id)
    )

def delete_customer(customer_id):
    execute_query("DELETE FROM customers WHERE customer_id = %s", (customer_id,))


# CRUD for Orders
def get_orders():
    return execute_query(
        """
        SELECT o.order_id, o.customer_id, o.order_date, o.total_price, b.title AS book_title 
        FROM orders o
        JOIN books b ON o.book_id = b.book_id
        """,
        fetchall=True, dictionary=True
    )

def place_order(customer_id, book_id, total_price):
    execute_query(
        "INSERT INTO orders (customer_id, book_id, total_price) VALUES (%s, %s, %s)",
        (customer_id, book_id, total_price)
    )

def delete_order(order_id):
    execute_query("DELETE FROM orders WHERE order_id = %s", (order_id,))


# Search Books
def search_books(query):
    return execute_query(
        """
        SELECT book_id, title, price, stock 
        FROM books 
        WHERE title LIKE %s
        """,
        ('%' + query + '%',),
        fetchall=True, dictionary=True
    )

def get_book_details(book_id):
    return execute_query(
        """
        SELECT book_id, title, price, stock
        FROM books
        WHERE book_id = %s
        """,
        (book_id,),
        fetchone=True, dictionary=True
    )
