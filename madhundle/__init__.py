import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='madhundle_secret_key')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

#    # a simple page that says hello
#    @app.route('/hello')
#    def hello():
#        return 'Hello, World!'

    # import base site functionality
    from . import site
    app.register_blueprint(site.bp)

    # import mail extension
    from .extensions import mail
    app.config.from_mapping(
        MAIL_SERVER='smtp.madhundle.com',
        MAIL_PORT=587,
        MAIL_USERNAME='no-reply@madhundle.com',
        MAIL_PASSWORD='no-replyMH',
        MAIL_DEFAULT_SENDER='no-reply@madhundle.com')
    mail.init_app(app)

    return app

