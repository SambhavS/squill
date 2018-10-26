from flask import Flask, request, render_template
import random
import json
from gamelogic import core_game
app = Flask(__name__)

# Super Global
index_to_col = {0: "red", 1: "blue"}
file_states = dict()
user_col_states = dict()
full_game_state = dict()
reset_state = dict()

@app.route("/reset/<num>")
def reset(num):
    del file_states[num]
    del user_col_states[num]
    del full_game_state[num]
    return "reset button clicked"

@app.route("/online/<num>")
def online(num):
    return render_template("test.html")

@app.route("/docs/<num>")
def docs(num):
    return render_template("docs.html")

@app.route("/upload/<num>", methods=['POST'])
def upload(num):   
    if num not in file_states:
        file_states[num] = dict()
    if num not in user_col_states:
        user_col_states[num] = []
    username, code_text = request.form["username"], request.form["code_text"]
    if username not in file_states[num] and len(file_states[num]) == 2:
        return "Too many users: code was not submitted"
    file_states[num][username] = code_text
    if username not in [uname for color, uname in user_col_states[num]]:
        color = "blue" if any(["red" in tup for tup in user_col_states[num]]) else "red"
        user_col_states[num].append((color, username))
    return json.dumps(user_col_states[num])

@app.route("/info/<num>")
def info(num):
    if num in user_col_states:
        return json.dumps(user_col_states[num])
    return json.dumps([])

@app.route("/init/<num>")
def game(num):  
    if num not in full_game_state:
        full_game_state[num] = []
    red_code = list(file_states[num].items())[0][1]
    blue_code = list(file_states[num].items())[1][1]
    boards = core_game(red_code, blue_code, full_game_state[num])
    return json.dumps(boards)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

