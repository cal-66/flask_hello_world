#-------- Flask Hello World ----#
#__ import the Flask class from the flask package
from flask import Flask

#__ create the application object
app = Flask(__name__)

#__error handling: enable debugging
app.config["DEBUG"] = True

#__ use the decorator pattern to 
#__ link the view function to a url
@app.route("/")
@app.route("/hello")

#__ define the view using a function, which returns a string
def hello_world():
	return "Hello, World!?!?!?!?!"

#__ dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found",404



#__ start the development server using the run() method
if __name__ == "__main__":
	app.run()