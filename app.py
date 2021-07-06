import slack 
import os 
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
import requests

env_path = Path('.') / '.env'
app = Flask(__name__)
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# client.chat_postMessage(channel='#test', text="Hello")

@app.route('/get_date', methods=['POST','GET'])
def get_date():
    data = request.form
    user_name =data.get('user_name')
    url = data.get('text')
    text = f'The request is from: {user_name} for url:{url}'
    client.chat_postMessage(channel='#data-ops', text=text)
    requests.get('https://hook.integromat.com/kbe5u7e7t6niwpolnc4wt7ma6kntps4a?url={}'.format(url))
    return Response(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True , port=8080)
