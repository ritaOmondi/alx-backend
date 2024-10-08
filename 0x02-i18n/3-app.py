#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select the best match for the supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the home page
    """
    return render_template('3-index.html', title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
