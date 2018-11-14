import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author INTEGER, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year,isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author,year,isbn))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * from book')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title ="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * from book where title = ? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
    rows = cur.fetchall()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",  (title, author, year, isbn,id))
    conn.commit()
    conn.close()




#insert("Harry Potter and the Soccerer/'s Stone", 'JK ROWLING', 2000, 111111)
#insert("Harry Potter and the Chamber of Secrets", 'JK ROWLING', 2002, 123456)
#insert("Harry Potter and the Prisoner of Azkaban", 'JK ROWLING', 2004, 198765)
#insert("Harry Potter and the Order of Phoneix", 'JK ROWLING', 2006, 876543)



#print(view())
