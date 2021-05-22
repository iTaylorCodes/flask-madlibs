from flask import Flask, render_template, request
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def madlib_form():
    """Generate a form to submit madlib words."""

    inputs = story.prompts

    return render_template('form.html', prompts=inputs)

@app.route('/story')
def show_story():
    """Shows the story result."""

    story_text = story.generate(request.args)

    return render_template('story.html', text=story_text)