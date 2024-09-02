from flask import Flask, request, jsonify
from flask_restful import Api, Resource 

app = Flask(__name__)
# api = Api(app)
# We are wrapping our App in an API, initialises resful API

#class HelloWorld(Resource):
    #def get(self):
        #return {"message":"Hello World"}

@app.route("/", methods=["GET"])
def test():
    if request.method == "GET":
        return jsonify({"response": "Hello There!"})
    
# The response need to be in a valid JSON format
# This creates a dictionary with a key "message" and a value "Hello World". 
    
# api.add_resource(HelloWorld, "/")
    # or /helloworld 
        
if __name__ == "__main__":
    app.run(debug=True)
# starts our server and our flask appliciation
# debug starts it in debug mode, allos us to see logs and what is wrong


