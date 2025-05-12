from flask import Flask, request, jsonify, render_template, url_for, redirect

app = Flask(__name__)

# Root route to render the UI
@app.route('/')
def home():
    return render_template('index3.html')

# Route for handling GET requests
@app.route('/get', methods=['GET'])
def handle_get():
    return jsonify({"message": "This is a GET request"})

# Route for handling POST requests
@app.route('/post', methods=['POST'])
def handle_post():
    data = request.form.get('data')  # Get data from the form
    return jsonify({"message": "This is a POST request", "data": data})

# Route with both GET and POST methods
@app.route('/both', methods=['GET', 'POST'])
def handle_both():
    if request.method == 'GET':
        return jsonify({"message": "This is a GET request on /both"})
    elif request.method == 'POST':
        data = request.form.get('data')  # Get data from the form
        return jsonify({"message": "This is a POST request on /both", "data": data})

# Route to handle /hello with a query parameter
@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    return f"Hello, {name}!"

# Route to demonstrate URL building
@app.route('/redirect-to-hello')
def redirect_to_hello():
    # Redirect to the /hello route with a query parameter
    return redirect(url_for('say_hello', name='FlaskUser'))

if __name__ == '__main__':
    app.run(debug=True)