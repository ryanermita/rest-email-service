# Rest Email Service
A simple email service using HTTP


## Setup
1. Manual Setup
  * clone repo
  
  ```
  git clone https://github.com/ryanermita/rest-email-service.git 
  ```

  * Install the project dependencies.
  
  ```
  pip install -r src/requirements.txt
  ```

2. Using Docker
  * clone repo
  
  ```
  git clone https://github.com/ryanermita/rest-email-service.git 
  ```
  
  * build project containers
  
  ```
  docker-compose build
  ```
  
## Environment Variables
Use environment variable for config var.

The env variables below is base on [Flask-Mail](https://pythonhosted.org/Flask-Mail/):
* MAIL_SERVER
* MAIL_PORT
* MAIL_USE_SSL
* MAIL_USERNAME
* MAIL_PASSWORD
* MAIL_DEFAULT_SENDER

## Running the app
1. Manual running
  * run the python app
  
  ```
  python src/server.py
  ```
  
  * run the celery app
  
  ```
  python -m celery -A server.celery_app worker
  ```
  
2. Run via docker

  ```
  docker-compose up
  ```

## Sample
Sample request:

```json
 {
    "subject": "Sample Subject",
    "sender": "sender@email.com",
    "recipients": "recipient1@email.com, recipientN@email.com",
    "body": "Your message here."
}
```

*subject -  the subject of the email.

*sender - mail sender in email format.

*recipients - list of mail recipients separated by comma and in email format.

*body - the e-mail message.

Sample Response

```json
 {
    "success": true,
    "error": ""
}
```

*success - boolean if sending of email is successful or not.

*error - error description if an erro occured.
