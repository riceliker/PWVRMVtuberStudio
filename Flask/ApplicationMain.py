from flask import Flask
import os

from Config import getPort

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=getPort(), debug=True)