from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    script = request.args.get("script", None)
    if not script:
        return render_template('home.html')

    error = check_name(script.lower())
    if error:
        return error, 418
    
    return render_template('script.html', script=script)

def check_name(script):
    if 'a' in script:
        return f'"a"is not allowed'
                
    return None