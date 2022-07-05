from flask import Flask, request, send_file
import matplotlib.pyplot as plt
from colorizers import *

urls = ("/favicon.ico", "dummy")
app = Flask(__name__)

@app.route('/get', methods = ['GET'])
def hello():
    return "Hello World"

@app.route('/post', methods = ['POST'])
def getImage():
    file = request.files['file']
    
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()
    (tens_l_orig, tens_l_rs) = preprocess_img(file, HW=(256,256))
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

    response = {"Hello":"Success"}
    return response
    #return send_file(out_img_siggraph17)

if __name__ == '__main__':
    app.debug = True
    app.run()