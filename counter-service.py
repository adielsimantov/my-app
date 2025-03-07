 #!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
post_counter = 0
get_counter = 0
@app.route('/add', methods=["POST", "GET"])
def index():
    global post_counter, get_counter 
    if request.method == "POST":
        post_counter+=1
        return "Hmm, Plus 1 please "
    elif request.method == "GET":
        get_counter+=1
        return "Hmm, Plus 1 please "

@app.route('/show', methods=["GET"])
def show_counter():
 return str(f"GET counter has {get_counter} and POST counter has {post_counter}")

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
