import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)

def create_products(conn):
    create_product(conn, ('eyeshadow palette', 35.50, 5))  # 1
    create_product(conn, ('lip liner', 25.00, 10))  # 2
    create_product(conn, ('face powder ', 120.00, 8))  # 3
    create_product(conn, ('blush', 62.40, 12))  # 4
    create_product(conn, ('face primer', 20, 5))  # 5
    create_product(conn, ('highlighter', 600.99, 2))  # 6
    create_product(conn, ('skin foundation', 108.60, 7))  # 7
    create_product(conn, ('brow gel', 400, 20))  # 8
    create_product(conn, ('lipstick', 250.00, 6))  # 9
    create_product(conn, ('under-eye concealer ', 105000.00, 3))  # 10
    create_product(conn, ('cream', 114.59, 4))  # 11
    create_product(conn, ('exfoliant', 19.40, 8))  # 12
    create_product(conn, ('mirror', 73.70, 4))  # 13
    create_product(conn, ('cleansing wipes ', 250.00, 3))  # 14
    create_product(conn, ('moisturizer', 240.00, 5))  # 15



def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error as e:
        print(e)


def search_by_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


connection = create_connection(r"hw.db")
create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print('Connected successfully')
    create_table(connection, create_products_table)
    create_product(connection, (29.80, 5))
    update_product_quantity(connection, (8, 1))
    update_product_price(connection, (29.80, 5))
    delete_product(connection, 1)
    print_all_products(connection)
    print('---------------------------')
    search_by_price_and_quantity(connection)
    print('---------------------------')
    search_by_word(connection, 'мыло')
    print('---------------------------')


