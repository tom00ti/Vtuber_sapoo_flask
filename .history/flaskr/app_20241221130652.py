from flask import Flask, render_template

app = Flask(__name__)

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

def form():
    

if __name__ == '__main__':
    app.run(debug=True)
