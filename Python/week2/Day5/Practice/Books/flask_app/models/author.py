from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM authors"
        resutls = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for u in resutls :
            authors.append(cls(u))
        return authors
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(fname)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL(DATABASE).query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors
