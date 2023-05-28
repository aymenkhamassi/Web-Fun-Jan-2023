from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self,data,):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_specefic(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results  = connectToMySQL(DATABASE).query_db(query,data)

        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        print(all_users)
        return all_users
    
    @classmethod
    def create(cls,data):

        query = """
        INSERT INTO ninjas (first_name, last_name,age,dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
