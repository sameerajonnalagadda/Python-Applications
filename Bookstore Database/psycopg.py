import psycopg2

def create():
    conn = psycopg2.connect("dbname = 'psycopg' user = 'postgres' password = 'hfdabS14' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'psycopg' user = 'postgres' password = 'hfdabS14' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

insert("table", 8, 15)

def view():
    conn = psycopg2.connect("dbname = 'psycopg' user = 'postgres' password = 'hfdabS14' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname = 'psycopg' user = 'postgres' password = 'hfdabS14' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname = 'psycopg' user = 'postgres' password = 'hfdabS14' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

#update(11, 6, 'Wine Glass')



#print(view())


#create()
