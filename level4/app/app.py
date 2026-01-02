from flask import Flask, render_template, request
import base64
import re
import urllib.parse

SVG_R = r'(?:<\?xml\b[^>]*>[^<]*)?(?:<!--.*?-->[^<]*)*(?:<svg|<!DOCTYPE svg)\b'
SVG_RE = re.compile(SVG_R, re.DOTALL)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    image = request.args.get("image", None)
    if not image:
        return render_template('home.html')
    
    try:
        image = base64.urlsafe_b64decode(image + '==').decode('utf-8', 'ignore')
        if SVG_RE.match(image):
            return render_template('image.html', image=image)
        else:
            return "SVG file not supported."
    except base64.binascii.Error as e:
            return str(e)