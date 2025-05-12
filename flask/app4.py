from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def greet_user():
    name = request.args.get('name')
    city = request.args.get('city')

    if name and city:
        return render_template('greeting.html', name=name, city=city)
    else:
        return '''
            <form action="/" method="get">
                Name: <input type="text" name="name"><br>
                City: <input type="text" name="city"><br>
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
