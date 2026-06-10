# database.py

import sqlite3
import os

DB_PATH = "data/ecommerce.db"

# DATABASE CONNECTION
def get_connection():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


# INITIALIZE DATABASE
def initialize_db():

    conn = get_connection()
    cursor = conn.cursor()

    with open("schema.sql", "r") as file:
        cursor.executescript(file.read())

    conn.commit()
    conn.close()

    print("✅ Database initialized successfully!")


# ==============================
# USER FUNCTIONS
# ==============================

def add_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            INSERT INTO users(name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password))

        conn.commit()

        print("✅ User added successfully!")

    except sqlite3.IntegrityError:

        print("❌ Email already exists!")

    conn.close()


def view_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    conn.close()

    return users


def search_user(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE name LIKE ?
        OR email LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))

    results = cursor.fetchall()

    conn.close()

    return results


def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE id = ?
    """, (user_id,))

    conn.commit()

    if cursor.rowcount > 0:

        print("✅ User deleted successfully!")

    else:

        print("❌ User not found!")

    conn.close()


# ==============================
# PRODUCT FUNCTIONS
# ==============================

def add_product(name, category, price, stock):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products(name, category, price, stock)
        VALUES (?, ?, ?, ?)
    """, (name, category, price, stock))

    conn.commit()

    print("✅ Product added successfully!")

    conn.close()


def view_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return products


def search_product(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE ?
        OR category LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))

    results = cursor.fetchall()

    conn.close()

    return results


def delete_product(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    conn.commit()

    if cursor.rowcount > 0:

        print("✅ Product deleted successfully!")

    else:

        print("❌ Product not found!")

    conn.close()


# ==============================
# CART FUNCTIONS
# ==============================

def add_to_cart(user_id, product_id, quantity):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cart(user_id, product_id, quantity)
        VALUES (?, ?, ?)
    """, (user_id, product_id, quantity))

    conn.commit()

    print("✅ Product added to cart!")

    conn.close()


def view_cart():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT cart.id,
               users.name AS user_name,
               products.name AS product_name,
               cart.quantity
        FROM cart
        JOIN users ON cart.user_id = users.id
        JOIN products ON cart.product_id = products.id
    """)

    items = cursor.fetchall()

    conn.close()

    return items


# ==============================
# ORDER FUNCTIONS
# ==============================

def place_order(user_id, total_amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders(user_id, total_amount)
        VALUES (?, ?)
    """, (user_id, total_amount))

    conn.commit()

    print("✅ Order placed successfully!")

    conn.close()


def view_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT orders.id,
               users.name,
               orders.total_amount,
               orders.order_date
        FROM orders
        JOIN users ON orders.user_id = users.id
    """)

    orders = cursor.fetchall()

    conn.close()

    return orders


# ==============================
# PAYMENT FUNCTIONS
# ==============================

def add_payment(order_id, payment_method, payment_status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO payments(order_id, payment_method, payment_status)
        VALUES (?, ?, ?)
    """, (order_id, payment_method, payment_status))

    conn.commit()

    print("✅ Payment added successfully!")

    conn.close()


def view_payments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payments")

    payments = cursor.fetchall()

    conn.close()

    return payments