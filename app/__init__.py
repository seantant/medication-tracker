"""App package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module
app.config.from_object('app.config')

# Tell our app about views and model. Tell pylint and pycodestyle to 
# ignore this coding style violation.
import insta485.views  # noqa: E402  pylint: disable=wrong-import-position
import insta485.model  # noqa: E402  pylint: disable=wrong-import-position