from flask import Flask, request, jsonify
from games import Games 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    if request.method == "GET":
        return jsonify({"response": "Hello There!"})
    
# GET request to retrieve all games 
@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(Games) 

# GET request to retrieve a game by it's positon
@app.route("/games/<int:position>", methods=["GET"])
def get_game(position):
    game = None #Assumes game not found
    for g in Games:
        if g["position"] == position:
            game = g # Game exists, so we assign it to game
            break # so stop looking
    if game:
        return jsonify(game, {"message": "Game retrieved successfully"}), 200
    else:
        return jsonify({"message": "Game not found"}), 404       

# POST request to add a new game
@app.route("/games", methods=['POST'])
def add_game():
    new_game = request.get_json()
    Games.append(new_game)
    return jsonify(new_game), 201

# DELETE request to delete a game by position
@app.route("/games/<int:position>", methods={"DELETE"})
def delete_game(position):
    game = None 
    for g in Games:
        if g["position"] == position:
            game = g 
            break 
    if game:
        Games.remove(game)
        return jsonify({"message": "Game deleted successfully"}), 200
    else:
        return jsonify({"message": "Game not found"}), 404  
    
# PUT request to ammend an entire game
@app.route("/games/<int:position>", methods={"PUT"})
def replace_game(position):
    game = None 
    for g in Games:
        if g["position"] == position:
            game = g 
            break 
    if game:
        updated_game = request.get_json()
        game.update(updated_game)
        return jsonify({"message": "Game updated successfully"}), 200
    else:
        return jsonify({"message": "Game not found"}), 404  
    
# PATCH request to partialy ammend a game
@app.route("/games/<int:position>", methods={"PATCH"})
def update_game(position):
    game = None 
    for g in Games:
        if g["position"] == position:
            game = g 
            break 
    if game:
        updated_data = request.get_json()
        game.update(updated_data)
        return jsonify(game, {"message": "Game updated successfully"}), 200
    else:
        return jsonify({"message": "Game not found"}), 404  
    
if __name__ == "__main__":
    app.run(debug=True)
