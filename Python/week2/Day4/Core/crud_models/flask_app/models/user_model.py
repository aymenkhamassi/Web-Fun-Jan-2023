from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):

        query = "SELECT * from users;"
        results  = connectToMySQL("table_user").query_db(query)

        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        return all_users


    @classmethod
    def create(cls,data):

        query = """
        INSERT INTO users (first_name, last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """

        result  = connectToMySQL("table_user").query_db(query, data)

        return result
    
    @classmethod
    def get_one(cls,data):

        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        result = connectToMySQL("table_user").query_db(query,data)
        return cls(result[0])
    


    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email= %(email)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL("table_user").query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from users where id=%(id)s;
        """
        return connectToMySQL("table_user").query_db(query,data)
    

    @classmethod
    def get_last(cls):

        query = """
        SELECT * FROM users ORDER BY id DESC LIMIT 1;
        """
        result = connectToMySQL("table_user").query_db(query)
        return cls(result[0])