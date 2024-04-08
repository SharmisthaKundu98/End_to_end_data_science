from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

#Home page user interface
# we are rendering a template of my homepage html template
@app.route("/")
def home_page():
    return render_template("index.html")  

# sending the details using http "POST" method in /math route
@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('result.html' , result = result)

# above things also we can do with using "POSTMAN"
# using "jsonify" to get the final result into a json format

@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")