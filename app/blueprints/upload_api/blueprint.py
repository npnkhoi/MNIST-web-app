from flask import Blueprint, render_template, request
import re
import base64
import numpy as np
import pickle
from skimage import io, color, transform

def preprocess(filename):
    img = color.rgb2gray(io.imread(filename))
    img = transform.resize(img, (28,28))
    img = 1 - img
    return img
 
def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    with open('output.png', "wb") as f:
        f.write(img_decode)
    return img_decode
 
# Load model
model = pickle.load(open('models/large.pkl', 'rb'))
 
upload_api = Blueprint('upload_api', __name__)
 
 
@upload_api.route('/upload/', methods=['POST'])
def upload():
    parse_image(request.get_data())
    img = preprocess('output.png').reshape(28**2)
    prediction = model.predict([img])[0]
    return str(prediction)