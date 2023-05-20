from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "hahahah"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
    session['username'] = request.form['name']
    session['location'] = request.form['dojo']
    session['favorite'] = request.form['fav']
    session['comments'] = request.form['com']
    
    return redirect("/result")

@app.route('/result')
def show_user():
    return render_template("result.html",name_on_template=session['username'], location_on_template=session['location'],favorite_on_template=
                           session['favorite'],comments_on_template=session['comments'])


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')







if __name__ == "__main__":
    app.run(debug = True)
