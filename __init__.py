import os
import sentry_sdk

from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask

from .config import Config

if Config.SENTRY_DSN:
    sentry_sdk.init(
        dsn=Config.SENTRY_DSN,
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0
    )


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import views
    from . import views
    app.register_blueprint(views.bp)
    # print(app.url_map)
    return app
