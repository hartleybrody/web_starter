# Welcome to your first Flask app :)

# Imports usually happen at the top of the file in Python. They load
# in all the other libraries that your code will be using, so that you
# can call the functions they define, or instantiate the classes they create.

# import the main class from the "Flask" library that we need to create our web application
from flask import Flask

# Create the variable `app` which is an instance of the Flask class that
# we just imported. Being an "instance of a class" is something pretty
# import to any kind of software development, but you don't need to know
# exactly what it means right now.
app = Flask(__name__)


# Some boilerplate code that just says "if you're running this from the command
# line, start here." Again, not critical to know what this means yet.
if __name__ == "__main__":
    app.debug = True
    app.run()
