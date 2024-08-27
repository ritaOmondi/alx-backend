#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_timezone
import pytz
from pytz.exceptions import UnknownTimeZoneError

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Returns the user dictionary if 'login_as' URL parameter is provided and valid.
    Otherwise, returns None.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages in the following order:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request headers
    4. Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    
    return request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone():
    """
    Determine the best match for supported time zones in the following order:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default timezone (UTC)
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)  # Validate the timezone
            return timezone
        except UnknownTimeZoneError:
            pass  # If invalid, fallback to user settings
    
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])  # Validate the timezone
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass  # If invalid, fallback to default timezone
    
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request():
    """
    Check if a user is logged in and set it globally using Flask's 'g' object.
    """
    g.user = get_user()

@app.route('/')
def index():
    """
    Route for the home page.
    """
    if g.user:
        welcome_message = _("logged_in_as") % {"username": g.user['name']}
    else:
        welcome_message = _("not_logged_in")
    
    return render_template('7-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
