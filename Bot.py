from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    response = generate_response(user_message)
    return jsonify({'response': response})

def generate_response(user_message):
    # Simple response logic (you can replace this with NLP logic)
    if 'hello' in user_message.lower():
        return 'Hello! How can I assist you today?'
    else:
        return 'I am not sure how to respond to that.'

if __name__ == '__main__':
    app.run(debug=True)
