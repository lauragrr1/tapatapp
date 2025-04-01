from flask import Flask, request, jsonify
from serverP3 import DAOUser

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('identifier')
    password = data.get('password')
    user = DAOUser.login(identifier, password)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="10050")
