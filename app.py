from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple database (temporary)
users = [
    {"username": "admin", "password": "1234"},
    {"username": "user", "password": "abcd"}
]

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check user
    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"message": "Login Successful ✅"})
    
    return jsonify({"message": "Invalid Username or Password ❌"})

if __name__ == "__main__":
    app.run(debug=True)