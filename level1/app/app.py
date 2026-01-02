from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get("name", None)
    if not name:
        return render_template('home.html')
    
    return render_template('name.html', name=name)

@app.route('/echo', methods=['GET'])
def echo():
    string = request.args.get("string", None)    
    return '{"echo":"'+string+'"}'