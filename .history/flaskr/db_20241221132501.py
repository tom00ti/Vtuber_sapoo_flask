import sqlite3

DATABASE = 'database.db'

def creat_books_table():
    con = sqlite3.connect(DATABASE)