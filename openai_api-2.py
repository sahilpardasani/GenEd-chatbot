from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # This is necessary to handle CORS if your Flutter app and this backend are on different domains.

OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'
API_KEY = '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'  # Replace with your OpenAI API key

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data.get('prompt')
    messages_list = data.get('messages', [])  # Extract messages from the request, default to empty list if not present

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Adjusted for the Chat API
    payload = {
        "model": "gpt-3.5-turbo",  # You can adjust the model if needed
        "messages": messages_list,
        "max_tokens": 150,  # For example, limit the response to 150 tokens
        "temperature": .5
    
    }

    response = requests.post(OPENAI_API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        # Getting the assistant's reply for the Chat API
        assistant_reply = response_data['choices'][0]['message']['content']
        return jsonify({'data': assistant_reply.strip()})
    else:
        return jsonify({'error': 'Failed to fetch response from OpenAI'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)

