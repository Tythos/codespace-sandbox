"""
"""

import json
import flask
from gevent import pywsgi

APP = flask.Flask("codespace-sandbox")

@APP.route("/state")
def state():
    """
    """
    return json.dumps({
        "board": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    }), 200, {
        "Content-Type": "text/plain"
    }

@APP.route("/")
def index():
    """
    """
    return b"OK", 200, {
        "Content-Type": "text/plain"
    }

@APP.route("/ui/<path>")
def ui(path):
    """
    """
    return flask.send_from_directory("./public", path)

def main():
    """
    KIRK WTF WERE YOU THINKING HERE...!!!
    """
    pywsgi.WSGIServer(("0.0.0.0", 8000), APP).serve_forever()

if __name__ == "__main__":
    main()
