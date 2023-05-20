from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def part():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')



@app.route('/4')
def part1():
    return render_template("index.html",row=8,col=4,color1='red',color2='black')



@app.route('/<int:x>/<int:y>')
def part2(x,y):
    return render_template("index.html",row= x,col= y,color1='red',color2='black')


@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def part3(x,y,one,two):
    return render_template("index.html",row= x,col= y,color1=one,color2=two)






if __name__=="__main__":
    app.run(debug=True)