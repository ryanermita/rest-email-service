from flask_mail import Mail, Message
import celery_client

mail = Mail()
celery = celery_client.Celery()

def init_mailer(app):
  mail.init_app(app)

@celery.task(name="tasks.send_email")
def send_email(data):
    msg = Message(sender=data['sender'],
                  recipients=to_list(data['recipients']),
                  subject=data['subject'],
                  body=data['body'])
    mail.send(msg)

    return True


def to_list(r):
  return r.split(',')
