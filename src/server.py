from flask import Flask, request, jsonify
from utils import email_client, validation
import config

app = Flask(__name__)
app.config.from_object(config)
email_client.init_mailer(app)

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
    email_client.send_email(request.json)
    return jsonify({'success': True} )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
