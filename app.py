from helper.openai_api import text_completion
from helper.twilio_api import send_message

from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/bot', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        print("MESSAGE", message)

        # Get response from Openai
        result = text_completion(message)
        print("RESULT", result)
        if result['status'] == 1:
            print("SENDING MSG")
            send_message(sender_id, result['response'])
    except:
        print("HELLO WORLD")
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)
