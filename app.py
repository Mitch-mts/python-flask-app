from flask import Flask

# creates a flask application instance named app
app = Flask(__name__)


#defines a route that maps the root url of the app to helloWorld function
@app.route('/')
def helloWorld(): #function defines logic for handling requests to root url
    return "Hello, from your flask app!"

# this ensures app.run method is only called when the script is executed directly 
if __name__ == '__main__':
    app.run(debug=True) # this starts the flask dev server  and debug=True enables features like auto code reloading during dev
