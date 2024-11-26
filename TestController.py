from flask import Flask, request, jsonify

from UserService import user_service
from User import User

app = Flask(__name__)

@app.route('/test', methods = ['GET'])
def get_all_users():
    return ["John","Jerry","Matthew"]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5002')