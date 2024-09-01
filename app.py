from flask import Flask
from flask_restful import Api, Resource 

app = Flask(__name__)
api = Api(app)
# We are wrapping our App in an API, initialises resful API

if __name__ == "__main__":
    app.run(debug=True)
# starts our server and our flask appliciation
# debug starts it in debug mode, allos us to see logs and what is wrong

msg = "Hello World!"
print(msg)
