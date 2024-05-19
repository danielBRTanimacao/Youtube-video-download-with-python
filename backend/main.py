from flask import Flask

# init
app = Flask(__name__)

# route
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

# execute
app.run(debug=True)