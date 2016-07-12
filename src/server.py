from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from utils import validation, celery_client
from celery import Celery
import config
import logging


app = Flask(__name__)
app.config.from_object(config)
#Mail
mail = Mail()
mail.init_app(app)
#celery
celery_app = celery_client.make_celery(app)
#logging
logger = logging.getLogger('info')
logger.setLevel(logging.INFO)

@app.route('/')
def index():
    resp = {'app version': 1.0,
            'app name': 'restful email',
            'developer': 'Ryan Ermita'}
    return jsonify(resp)


@app.route('/email/send', methods=['POST'])
@validation.is_content_type_json
@validation.is_all_field_present
@validation.is_required_field_not_empty
@validation.is_sender_a_valid_email
@validation.is_recipients_a_valid_email
def send():
    send_email.apply_async(args=[request.json])
    return jsonify({'success': True, 'error': ''}), 200


@celery_app.task(name='send_email')
def send_email(data):
    logger.info("**************EMAIL PARAMETERS********")
    logger.info("sender: %s" % data['sender'])
    logger.info("recipients: %s" % to_list(data['recipients']))
    logger.info("Subject: %s" % data['subject'])
    logger.info("body:")
    logger.info(data['body'])
    logger.info("***************************************")
    msg = Message(sender=data['sender'],
                  recipients=to_list(data['recipients']),
                  subject=data['subject'],
                  body=data['body'])
    logger.info("*********SENDING EMAIL...***********")
    mail.send(msg)
    logger.info("*********EMAIL SENT*****************")

    return True


def to_list(r):
  return r.split(',')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3007)
