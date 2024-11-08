from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = f"Your message was: {user_message}. This is a sample response."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
