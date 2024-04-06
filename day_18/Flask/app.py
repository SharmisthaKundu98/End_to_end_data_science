from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello1")
def hello_world1():
    return "Hello World!1"

@app.route("/search")
def request_input():
    data = request.args.get("query")
    return "this is my query from url is :{}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")