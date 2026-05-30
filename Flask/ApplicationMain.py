# Library
from flask import Flask
from multiprocessing import Process, Queue
import os

# Application
app = Flask(__name__)

# Config
from Config import getPort

# Controller
from Controller.test import bp as test_bp
app.register_blueprint(test_bp)

from Controller.CameraOperation import bp as camera_bp
app.register_blueprint(camera_bp, url_prefix="/camera")

# OpenCV

# Service

# DataBase

# MultiProcess

def addProcess(func,arg_list):
    p = Process(target=func, args=arg_list)
    p.start()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=getPort(), debug=False)
    
    