from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "the secret"

# debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    
    all_prompts = story.prompts
    
    return render_template('homepage.html',prompts=all_prompts)

@app.route('/story')
def show_story():
    
    result= story.generate(request.args)
    
    return render_template('story.html',result=result)
