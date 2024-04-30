from flask import Blueprint, render_template, flash, current_app, request, redirect, url_for
#from flask_mail import Message
#from .extensions import mail

bp = Blueprint('site', __name__, template_folder="templates", static_folder="static")

@bp.route('/', methods=['GET'])
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

@bp.route('/', methods=['POST'])
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

    return redirect(url_for('site.index'))


