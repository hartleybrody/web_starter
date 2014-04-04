# Welcome to your first Flask app :)

# Imports usually happen at the top of the file in python. They load
# in all the other libraries that your code will be using, so that you
# can call the functions they define, or instantiate the classes they create.

# import the main class from the "Flask" library that we need to create our web application
from flask import Flask

# Create the variable `app` which is an instance of the Flask class that
# we just imported. Being an "instance of a class" is something pretty
# import to any kind of software development, but you don't need to know
# exactly what it means right now.
app = Flask(__name__)


# Here, we're creating the homepage of our application. We're defining a
# function called `homepage` which doesn't take any arguments (nothing
# inside the parentheses). Above the function definiton, we're adding a
# "decorator" which tells our app which "route" (ie URL) should be mapped
# to this function. So if you wanted to add more pages to your app, you
# could add new python functions for them, and decorate them with new routes.
@app.route("/")
def homepage():
    
	# Inside this function, you can run whatever logic you want, running any python
	# code your heart desires. You could check the cookies on the request to see if
	# there's a logged in user making the requests, you could read or write to a
	# database or run any kind of functions you want.
    return "Hello World"


# Some boilerplate code that just says "if you're running this from the command
# line, start here." Again, not critical to know what this means yet.
if __name__ == "__main__":
    app.debug = True
    app.run()
