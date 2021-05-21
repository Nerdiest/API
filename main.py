from flask import Flask, request
from flask_cors import CORS, cross_origin
import config
app = Flask(__name__)
app.config["DEBUG"] = config.server["debug"]
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/v1/tools": {"origins": "https://nerdiest.io"}})


@app.route('/v1/tools', methods=['POST'])
@cross_origin(origin='https://nerdiest.io',headers=['Content- Type','Authorization'])
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


app.run(host=config.server['host'], ssl_context=('certificate.crt', 'private.key'))
