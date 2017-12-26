from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import flask
from flask import request
from flask import make_response

# Flask app should start in gobal layout
app = Flask (__name__)

@app.route('/webhook', methods = ['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent = 4))

    res = processrequest(req)

    res.headers['content-Type'] = 'application/json'
    return res

def processrequest(req):
    print("Request")
    print(json.dumps(req, indent =4))
    age = data.get("result").get("parameters").get("age").get("amount")
    if age > 30 & age < 130:
        speech = "你超老!但是你還是人~"
    elif age < 30 & age>0:
        speech = "肖廉欸!去讀期末啦!"
    else:
        speech = "你是人嗎!"

    return{
        "speech": speech,
        "displayText": speech,
        "source": "webhookdata"
    }
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" %port)

    app.run(debug=False, port = port, host = '0.0.0.0')
