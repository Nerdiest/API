from flask import Flask, request, jsonify
import config
app = Flask(__name__)
app.config["DEBUG"] = config.server["debug"]


@app.route('/api/v1/tools', methods=['POST'])
def handle():
    from handler import Handler
    data = request.get_json()
    if 'call' not in data:
        return "Error: No call provided"
    call = data["call"]
    type = data["type"]
    params = data["params"]

    res = Handler(call, type, params)
    return res.handle()


@app.route('/', methods=['GET'])
def home():
    return "<img src='https://media4.giphy.com/media/8abAbOrQ9rvLG/200.gif' style='width:100%'>"


app.run()