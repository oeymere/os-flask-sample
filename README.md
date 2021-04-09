# Sample Appication for Open Shift Deployment
This repository is a very simple flask application to test out deploying
python applications to Open Shift.

This application uses the openweathermap.org weather api and you must supply an
API key which can be obtained by registering for an account at:
https://home.openweathermap.org/users/sign_up

To run the application locally you will need python v3+ installed.  From the
parent directory of this repository run:
    $ python3 -m venv os-flask-sample

  switch to the virtual env by running:
    $ source os-flask-sample/bin/activate

  Install the required python libraries:
    $ python -m pip install -r os-flask-sample/requirements.txt

  Run the application:
    $ export FLASK_APP=main.py

    # Optional to run server in debug mode
    $ export FLASK_ENV=development

    $ flask run -h 0.0.0.0

When deploying to OpenShift the following configuration variable must be set in
the environment:
  * SECRET_KEY - Set in secrets
    To create a secret key run in a python shell:
    >>> import os
    >>> os.urandom(24)
  * WEATHER_API_KEY - Your open weather map API key
  * FLASK_ENV=development - To run the flask server in debug mode