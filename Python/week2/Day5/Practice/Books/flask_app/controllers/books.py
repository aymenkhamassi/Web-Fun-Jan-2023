from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.book import Book
from ..models.author import Author


@app.route('/books')
def create_book():
    books = Book.get_all_books()
    return render_template("books.html",books = books)


@app.route('/create/books',methods = ['POST'])
def show_books():
    data = {
        "btitle": request.form["btitle"],
        "bpage" : request.form["bpage"]
    }
    Book.save_books(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    return render_template('book_show.html',book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")