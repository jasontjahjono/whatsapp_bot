from helper.openai_api import generate_reply
from helper.twilio_api import send_message

from dotenv import load_dotenv
from flask import Flask, request
load_dotenv()

app = Flask(__name__)


@app.route('/')
def sanity_check():
    return 'Just Checking!'


@app.route('/msg', methods=['POST'])
def receive_message():
    try:
        msg_body = request.form['Body']
        sender_id = request.form['From']

        # Call OpenAI Api
        result = generate_reply(msg_body)

        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)
