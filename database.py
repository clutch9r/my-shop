import sqlite3

def init_db():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS categories
                 (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, name TEXT, price TEXT,
                  description TEXT, photo_id TEXT, category_id INTEGER)''')
    conn.commit()
    conn.close()

def add_category(name):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('INSERT INTO categories (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def get_categories():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('SELECT * FROM categories')
    rows = c.fetchall()
    conn.close()
    return rows

def add_product(name, price, description, photo_id, category_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('INSERT INTO products (name, price, description, photo_id, category_id) VALUES (?,?,?,?,?)',
              (name, price, description, photo_id, category_id))
    conn.commit()
    conn.close()

def get_products(category_id=None):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    if category_id:
        c.execute('SELECT * FROM products WHERE category_id=?', (category_id,))
    else:
        c.execute('SELECT * FROM products')
    rows = c.fetchall()
    conn.close()
    return rows
