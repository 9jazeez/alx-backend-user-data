#!/usr/bin/env python3
""" A module for flask app """

from flask import Flask, jsonify, request
from auth import Auth

Auth = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def status():
    """First get method """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
   """ Register users """
   try:
       email = request.form.get("email")
       password = request.form.get("password")
       query = Auth.register_user(email, password)
       return jsonify({"email": email, "message": "user created"})
   except ValueError:
       return jsonify({"message": "email already registered"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
