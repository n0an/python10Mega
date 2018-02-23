import psycopg2

def create_table():
    conn = psycopg2.connect(database_credential)

    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(database_credential)
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')"% (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view_db():
    conn = psycopg2.connect(database_credential)
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_from_db(item):
    conn = psycopg2.connect(database_credential)
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect(database_credential)
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))
    conn.commit()
    conn.close()

database_credential = "dbname='postgres' user='postgres' password='5432' host='localhost' port='5432'"

# create_table()
#
# insert("orange", 30, 20)

print(view_db())

# delete_from_db('orange')

# update(40, 1, 'apple')
