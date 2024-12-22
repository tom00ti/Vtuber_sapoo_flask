import sqlite3

DATABASE = 'database.db'

def creat_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE books (title, price, arrival_day) ")