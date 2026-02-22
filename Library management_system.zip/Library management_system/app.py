from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

# Initialize database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT DEFAULT 'Available'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Handle Add Book
    if request.method == 'POST' and 'add_book' in request.form:
        title = request.form['title']
        author = request.form['author']
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()

    # Handle Issue Book
    if request.args.get('issue'):
        book_id = request.args.get('issue')
        cursor.execute("UPDATE books SET status='Issued' WHERE id=?", (book_id,))
        conn.commit()

    # Handle Return Book
    if request.args.get('return'):
        book_id = request.args.get('return')
        cursor.execute("UPDATE books SET status='Available' WHERE id=?", (book_id,))
        conn.commit()

    # Handle Delete Book
    if request.args.get('delete'):
        book_id = request.args.get('delete')
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()

    # Fetch all books
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)