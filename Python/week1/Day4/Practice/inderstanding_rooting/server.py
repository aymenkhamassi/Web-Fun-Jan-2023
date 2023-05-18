from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/dojo')
def success():
  return "dojo"
  
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/35/hello/<int:times>')
def repeat(times):
    return "<h2> hello </h2>" * times

@app.route('/bye/<int:times>')
def bye(times):
    return "<h2> bye </h2>" * times


@app.route('/users/<username>/<id>') 
def show_user_profile(username, id):
    return "username: " + username + ", id: " + id





if __name__=="__main__":     
    app.run(debug=True)    


