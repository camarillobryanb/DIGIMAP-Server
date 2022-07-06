from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
import matplotlib.pyplot as plt
from colorizers import *

urls = ("/favicon.ico", "dummy")
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def colorize():
    if request.method == 'POST':
        image = request.files['file']

        filename = secure_filename(image.filename)
        image.save('static/images/'+filename)
        img = cv2.imread("static/images/"+filename)

        colorizer_siggraph17 = siggraph17(pretrained=True).eval()
        (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
        out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

        plt.imsave('static/output/'+filename, out_img_siggraph17)

        return render_template("index.html", filename=filename)

    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()