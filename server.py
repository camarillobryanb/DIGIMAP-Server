from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
import matplotlib.pyplot as plt
#from colorizers import *

urls = ("/favicon.ico", "dummy")
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def colorize():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()