from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Dojo:
    def __init__(self,data,):
        self.id  = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojo_and_ninja").query_db(query)
        dojos = []
        for u in results:
           dojos.append(cls(u))
        return dojos    
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(fname)s);"
        return connectToMySQL("dojo_and_ninja").query_db(query,data)
    

