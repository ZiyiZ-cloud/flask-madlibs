from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    html="""
    <html>
        <body>
        <h1>Homepage!</h1>
        <p> Welcome to my first app!</p>
        <a herf=`/hello`>Go to hello page</a>
        </body>
    </html>
    """
    return html