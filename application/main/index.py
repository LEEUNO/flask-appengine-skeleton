from application.main import main as app
from flask import url_for, redirect

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return redirect(url_for('static', filename="index.html"))


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.app_errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404


@app.app_errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500
