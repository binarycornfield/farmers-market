from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')

    if not user_id or not username:
        return jsonify({'error': 'Missing user_id or username'}), 400

    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400

    users[user_id] = {
        'user_id': user_id,
        'username': username
    }
    return jsonify({'message': 'User created successfully', 'user': users[user_id]}), 201
if __name__ == '__main__':
    app.run(debug=True)