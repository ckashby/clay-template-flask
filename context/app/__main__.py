from soffos.logging import configure_logger
from waitress import serve

import settings


if __name__ == '__main__':
    configure_logger(level='DEBUG' if settings.DEBUG else settings.LOG_LVL)
    from web import app
    if settings.DEBUG:
        app.run(host=settings.APP_HOST, port=settings.APP_PORT)
    else:
        serve(app, host=settings.APP_HOST, port=settings.APP_PORT)
