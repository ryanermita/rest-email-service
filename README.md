# Rest Email Service
A simple email service using HTTP


## Setup
* Manual Setup
   1. clone repo
  
   ```
   git clone https://github.com/ryanermita/rest-email-service.git 
   ```

   2. Install the project dependencies.
  
   ```
   pip install -r src/requirements.txt
   ```

* Using Docker
   1. clone repo
  
   ```
   git clone https://github.com/ryanermita/rest-email-service.git 
   ```
  
   2. build project containers
  
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
