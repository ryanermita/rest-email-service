import os

#REDIS CONFIG
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
CELERY_BROKER_URL='redis://%s:%s' % (REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND='redis://%s:%s' % (REDIS_HOST, REDIS_PORT)

# MAILER CONFIG
MAIL_SERVER=os.environ.get('MAIL_SERVER')
MAIL_PORT=os.environ.get('MAIL_PORT')
MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL')
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAUL_SENDER')
