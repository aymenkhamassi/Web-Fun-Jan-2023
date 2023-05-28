from flask_app import app
from flask import request ,render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/ninjas')
def index():
    
    return render_template("new_ninja.html")


@app.route('/ninjas',methods = ['POST'])
def create_ninja():
    data = {
         "dojo_id" : request.form["dojo_id"],
         "fname" : request.form["fname"],
         "lname" : request.form["lname"],
         "age" : request.form["age"]
    }
    Ninja.save(data)
    return redirect('/')




        