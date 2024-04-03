from views import index, poll
from settings import BASE_DIR


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=BASE_DIR / 'aiohttpdemo_polls' / 'static',
                          name='static')


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/{question_id}', poll)
