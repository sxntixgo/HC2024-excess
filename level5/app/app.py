from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    image = request.args.get("image", None)
    if not image:
        return render_template('home.html')
    
    image = image.replace(' ', '+')
    return render_template('image.html', image=image)