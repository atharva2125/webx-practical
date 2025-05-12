from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def greet_user(name):
    return f"<h1>Hello, {name}! Welcome to our website.</h1>"

if __name__ == '__main__':
    app.run(debug=True)