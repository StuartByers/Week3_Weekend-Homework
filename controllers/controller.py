from flask import render_template, request, redirect

from app import app
from models.book_list import book_list, add_new_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title = 'Book List', books = book_list)

@app.route('/books/<id>')
def book(id):
    return render_template('book.html', title = 'Selected Book', my_book = book_list[int(id)])

@app.route('/books', methods=['POST'])
def add_book():
    print(request.form)
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('index.html', title='Book List', books = book_list)
    