from flask import jsonify, request
from functools import wraps
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

def is_content_type_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.content_type == 'application/json':
            return f(*args, **kwargs)

        resp = {'success': False,
                'error': 'Request Content-Type must be application/json'}
        return jsonify(resp), 403

    return decorated_function


def is_all_field_present(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        required_fields = ['sender', 'recipients', 'body', 'subject']
        payload = request.json
        
        # check if all key is present
        for r in required_fields:
            if r not in payload:
                resp = {'success': False,
                        'error': '%s is a required field for sending email.'% r}
                return jsonify(resp), 403
        return f(*args, **kwargs)
    return decorated_function


def is_required_field_not_empty(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        payload = request.json

        for p in payload:
            if not payload[p]:
                resp = {'success': False,
                        'error': '%s must not be empty.'% p}
                return jsonify(resp), 403
        return f(*args, **kwargs)
    return decorated_function


def is_sender_a_valid_email(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        payload = request.json
        email = payload['sender']

        if not is_valid_email(email):
            resp = {'success': False,
                    'error': 'Sender should be in email format.'}
            return jsonify(resp), 403
        return f(*args, **kwargs)
    return decorated_function


def is_recipients_a_valid_email(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        payload = request.json
        recipients = payload['recipients'].split(',')

        for r in recipients:
            if not is_valid_email(r):
                resp = {'success': False,
                        'error': '%s is not in email format. Recipients should be in email format.'% r}
                return jsonify(resp), 403

        return f(*args, **kwargs)
    return decorated_function


def is_valid_email(email):
    if not EMAIL_REGEX.match(email):
        return False

    return True
