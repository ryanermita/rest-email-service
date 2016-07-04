from flask_mail import Mail, Message

mail = Mail()

def init_mailer(app):
  mail.init_app(app)

def send_email(data):
    msg = Message(sender=data['sender'],
                  recipients=to_list(data['recipients']),
                  subject=data['subject'],
                  body=data['body'])
    mail.send(msg)

    return True


def to_list(r):
  return r.split(',')
