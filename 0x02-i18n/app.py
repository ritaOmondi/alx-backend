from flask import Flask, render_template
from flask_babel import Babel, gettext
from datetime import datetime

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Example locale selection logic
    return 'fr'  # This would be replaced with your locale logic

@app.route('/')
def index():
    # Get the current time
    now = datetime.now()
    # Format the current time based on the user's locale
    formatted_time = gettext('current_time_is', current_time=now.strftime('%b %d, %Y, %I:%M:%S %p'))
    return render_template('index.html', formatted_time=formatted_time)

if __name__ == '__main__':
    app.run()

