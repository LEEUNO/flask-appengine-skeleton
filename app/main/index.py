from . import main as app


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'testing'


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
