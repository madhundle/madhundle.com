# import os
from flask import Flask, render_template, current_app, url_for, request, redirect
# from site import bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    # app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='madhundle_secret_key')

    # Trying a simpler structure with no instance folder, no separate configs
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass


    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    def contactEmail(name, email, message):
        current_app.logger.debug("Emailing", name, email, message)
        # msg = Message("Contact Message from madhundle.com")
        # msg.recipients= ['mh@madhundle.com']
        # msg.html = "<style>body {background-color: #00BDBD; padding: 10px;}</style>"
        # msg.html += "<p> Name:&nbsp;&nbsp;" + name + "</p>"
        # msg.html += "<p> Email:&nbsp;&nbsp;" + email + "</p>"
        # msg.html += "<p style=\"white-space:pre-wrap;\">Message:&nbsp;&nbsp;<br>" + message + "</p>"
        # mail.send(msg)
        return

    @app.route('/', methods=['POST'])
    def contactPost():
        name = request.form.get('contactName')
        email = request.form.get('contactEmail')
        message = request.form.get('contactMessage')
        try:
            contactEmail(name, email, message)
    #        session['sent'] = True
    #        flash("Email sent!", 'alert-success')
        except Exception as e:
            current_app.logger.debug("Error while sending contact email")
            current_app.logger.error(e)
    #        session['sent'] = False
    #        flash("Email failed to send. Please try again soon.", 'alert-danger')

        return redirect(url_for('index'))
        # return redirect(url_for('site.index'))


    """
    This is all from a Blueprint configuration that kept having import errors
    Also, my app was a python package with __init__.py
    I'm going back to a simple App, no blueprint, no package just one module
    """
    # import base site functionality
    # from madhundle import site # Works on local dev but not deployment
    # from . import site # Works, but trying to not have relative imports
    # import site # Didn't work: AttributeError: module 'site' has no attribute 'bp'
    # import madhundle.site # Works on local dev, though VS Code gives an error
    # app.register_blueprint(site.bp) # type: ignore
    
    # trying with import bp directly, not all of site
    # app.register_blueprint(bp)

    # import mail extension
    # from madhundle.extensions import mail # Works, but commenting out for debugging
    # from .extensions import mail # Works, but trying not to have relative imports
    # app.config.from_mapping(
    #     MAIL_SERVER='smtp.madhundle.com',
    #     MAIL_PORT=587,
    #     MAIL_USERNAME='no-reply@madhundle.com',
    #     MAIL_PASSWORD='no-replyMH',
    #     MAIL_DEFAULT_SENDER='no-reply@madhundle.com')
    # mail.init_app(app)

    return app

# Do I ever need this?
# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)