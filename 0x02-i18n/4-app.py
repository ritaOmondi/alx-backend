#!/usr/bin/env python3
from flask import Flask, render_template, request
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
    Determine the best match for supported languages.
    Check if a 'locale' parameter is passed in the URL and return it if valid.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the home page
    """
    return render_template('4-index.html', title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
