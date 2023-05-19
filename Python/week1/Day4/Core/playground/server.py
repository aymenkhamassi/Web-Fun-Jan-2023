from flask import Flask,render_template
app = Flask(__name__)


@app.route("/play")
def level1():
    return render_template("index.html", phrase="blue", times=int(3))

@app.route("/play/<x>")
def level2(x):
    return render_template("index.html", phrase="blue", times=int(x))

@app.route("/play/<x>/<color>")
def level3(x,color):
    return render_template("index.html", phrase=color, times=int(x))







if __name__=="__main__":
    app.run(debug=True) 