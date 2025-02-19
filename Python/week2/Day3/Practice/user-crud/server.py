from flask import Flask, render_template, request, redirect

from user import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    return render_template("edit.html",user=User.get_one(data))



@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.destroy(data)
    return redirect('/users')






if __name__=="__main__":
    app.run(debug=True)