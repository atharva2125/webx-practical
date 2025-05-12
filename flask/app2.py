from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Root route to render the UI
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling GET requests
@app.route('/get', methods=['GET'])
def handle_get():
    return jsonify({"message": "This is a GET request"})

# Route for handling POST requests
@app.route('/post', methods=['POST'])
def handle_post():
    # Get JSON data from the form
    data = request.form.get('data')
    return jsonify({"message": "This is a POST request", "data": data})

# Route with both GET and POST methods
@app.route('/both', methods=['GET', 'POST'])
def handle_both():
    if request.method == 'GET':
        return jsonify({"message": "This is a GET request on /both"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "This is a POST request on /both", "data": data})

# Route to handle /hello with a query parameter
@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get('name', 'Guest')  # Default to 'Guest' if no name is provided
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)