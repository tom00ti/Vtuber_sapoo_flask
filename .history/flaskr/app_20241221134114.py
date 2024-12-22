from flask import Flask, render_template
import sqlite3
DATABASE = 'database.db'

app = Flask(__name__)

 from flaskr import db
# db.creat_books_table()

@app.route('/')
def index():
    books = [
        {
        'title': 'はらぺこあおむし',
        'price': 1200,
        'arrival_day': '2020/07/12'
        },
        {
        'title': 'ぐりとぐら',
        'price': 990,
        'arrival_day': '2020/07/13'
        }
    ]
    return render_template(
        'index.html',
        books=books
    )

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)