from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')

    return jsonify({'message': 'User created successfully', 'user': users[user_id]}), 201
if __name__ == '__main__':
    app.run(debug=True)