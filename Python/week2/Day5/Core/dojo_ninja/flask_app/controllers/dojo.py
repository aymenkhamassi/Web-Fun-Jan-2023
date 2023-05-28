from flask_app import app
from flask import request ,render_template,redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja




@app.route('/')
def index():
    
    return render_template("index.html",dojos = Dojo.get_all())


@app.route('/create',methods = ['POST'])
def create_dojo():
    data = {
        "fname" : request.form["fname"]
    }
    Dojo.save(data)
    return redirect('/')






