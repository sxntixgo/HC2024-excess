from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get("name", None)
    if not name:
        return render_template('home.html')
    
    name = filter_name(name.lower())
    return render_template('name.html', name=name)

def filter_name(name):
    filtered_name = name.replace("script", "")
    filtered_name = name.replace("img", "")
    if filtered_name == name:
        return filtered_name
    else:
        filter_name(filtered_name)