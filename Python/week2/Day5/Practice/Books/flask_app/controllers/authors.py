from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.author import Author
from ..models.book import Book


@app.route('/')
def index():
    return redirect('/authors')




@app.route('/authors')
def display_authors():
    authors = Author.get_all()
    return render_template("index.html",authors = authors)


@app.route('/create/author',methods = ['POST'])
def create():
    data = {
        "fname": request.form["fname"]
    }
    Author.save(data)
    return redirect('/')