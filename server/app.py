from flask import Flask

app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Prints to console
    return text  # Displays in browser

# Count Route (Fix: Ensure output ends with a newline)
@app.route('/count/<int:number>')
def count(number):
    return "\n".join(str(i) for i in range(number)) + "\n"

# Math Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/" or operation == "div":  # Accept both "/" and "div"
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


