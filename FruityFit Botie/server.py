from flask import Flask, request, jsonify
from Botie import Botie  # Assuming Botie is your custom chatbot class

chatbot = Botie()
app = Flask(__name__)

@app.route('/chat', methods=['POST', 'GET'])
def generate_chat():
    print(request)
    print(request.method)
    print(request.form)
    print(request.json)
    if request.method == 'POST':
        # Handle the POST request here
        input_user = request.json.get("user_input")  # Assuming the form field is named 'user_input'
        print(input_user)
        chatbot_response =  chatbot.answer_based_text_classification(input_user)

        # Prepare the response in JSON format
        response_data = {
             'user_input': input_user,
             'chatbot_response': chatbot_response
         }
        print(response_data)

        return jsonify(response_data)
    else:
        # Handle the GET request here
        return 'Hello, World'

if __name__ == '__main__':
    app.run(debug=True)
