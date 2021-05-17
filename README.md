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
Optional variables are:
  * FLASK_ENV=development - To run the flask server in debug mode

The application can be depoyed in OpenShift the following ways:
  * s2i: The project includes the .s2i/bin/ directory and a run script.  The existence of the requiremennts.txt file tips openshift that this is a python application.  To deploy via s2i run:
    $ oc new-app --as-deployment-config --name ${app_name} --strategy=source https://github.com/oeymere/os-flask-sample
    
  * Docker: The included Dockerfile will trigger openshift to build a docker image and deploy to the cluster.  To deploy via the docker strategy run:
    $ oc new-app --as-deployment-config --name ${app_name} -e SECRET_KEY='${your_secret_key}' -e WEATHER_API_KEY='${your_weather_api_key}' --strategy=docker https://github.com/oeymere/os-flask-sample
    
  * Template: A template can be found in the openshift_templates directory.  To deploy via a template run:
    $ oc new-app --file=flask_only_template.yaml -p SECRET_KEY='${your_secret_key}' -p WEATHER_API_KEY='${your_weather_api_key}'
