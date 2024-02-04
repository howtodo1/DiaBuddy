from flask import Flask, request, render_template
import time
from characterai import PyCAI

app = Flask(__name__)

@app.route("/")
def hello_world():
    client = PyCAI('[key here]')
    client.chat.new_chat('MqotBa3wzY3Bxyd6a1vbRu1hp_5nfbT263OtQoLGsW0')
    return render_template('index.html')


@app.route("/chat", methods=['POST'])
def chat():
    client = PyCAI('[key here]')
    chat = client.chat.get_chat("MqotBa3wzY3Bxyd6a1vbRu1hp_5nfbT263OtQoLGsW0")
    participants = chat['participants']
    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']
    data = request.json["test"]
    print(data)
    data1 = client.chat.send_message(
        chat['external_id'], tgt, data
    )
    return data1['replies'][0]['text']

app.run("0.0.0.0")
