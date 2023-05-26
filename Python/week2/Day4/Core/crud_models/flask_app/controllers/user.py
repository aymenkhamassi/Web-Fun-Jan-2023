from flask_app import app
from flask import request ,render_template,redirect
from flask_app.models.user_model import User

@app.route('/')
def index():
    users = User.get_all()

    return render_template("index.html",users = users)

@app.route('/users/new')
def new_user():
    return render_template("create.html")

@app.route('/users/create', methods=['POST'])
def create():
    User.create(request.form)
    last = User.get_last()
    return redirect('/users/'+str(last.id))

@app.route('/users/<int:user_id>')
def one_user(user_id):
    data = {
        'id':user_id
    }
    user = User.get_one(data)
    return render_template('read.html',user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user_to_update = User.get_one({'id':user_id})
    return render_template("edit.html",user=user_to_update)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "id":user_id
        }
    User.update(data)
    return redirect('/users/'+str(user_id))

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete({'id':user_id})
    return redirect('/')
