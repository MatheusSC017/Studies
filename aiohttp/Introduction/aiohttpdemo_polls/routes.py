from views import index, poll


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/{question_id}', poll)
