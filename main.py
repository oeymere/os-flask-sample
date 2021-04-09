from flask import Flask, render_template, request, Response
import requests
import os
import logging
import sys


app = Flask('flasksample')
app.config.from_object('config')
app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set.")
app.config['SECRET_KEY'] = SECRET_KEY

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
if not WEATHER_API_KEY:
    raise ValueError("No WEATHER_API_KEY set.")
app.config['WEATHER_API_KEY'] = WEATHER_API_KEY


@app.route('/', methods=['GET'])
def flasksample_root():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def weather_api():
    location = request.args.get('location')
    units = 'metric'
    app.logger.info("Getting weather for: " + location)
    if request.args.get('units') is not None:
        units = request.args.get('units')
        if units != 'metric' and units != 'imperial':
            app.logger.error("ERROR: Units parameter - " + units)
            return Response('{"error": "units must be metric or imperial"}',
                            status=400,
                            content_type='application/json')
    url = app.config['BASE_URL'] \
        + '?q=' + location \
        + '&units=' + units \
        + '&APPID=' + app.config['WEATHER_API_KEY']
    response = requests.get(url)
    app.logger.debug("Returing response: " + response.text)
    return Response(response.text, status=200, content_type='application/json')


@app.route('/weather_latlon', methods=['GET'])
def weather_by_latlon():
    units = 'metric'
    app.logger.info("Getting weather info for coordinates")
    if request.args.get('lat') is None or request.args.get('lon') is None:
        return Response('{"error": "request must include lat and lon"}',
                        status=400,
                        content_type='application/json')

    lat = request.args.get('lat')
    lon = request.args.get('lon')
    app.logger.info("Coordinates - Latitude: " + lat + " Longitude: " + lon)

    if request.args.get('units') is not None:
        units = request.args.get('units')
        if units != 'metric' and units != 'imperial':
            app.logger.error("ERROR: Units parameter - " + units)
            return Response('{"error": "units must be metric or imperial"}',
                            status=400,
                            content_type='application/json')

    url = app.config['BASE_URL'] \
        + '?lat=' + lat \
        + '&lon=' + lon \
        + '&units=' + units \
        + '&APPID=' + app.config['WEATHER_API_KEY']
    response = requests.get(url)
    app.logger.debug("Returing response: " + response.text)
    return Response(response.text, status=200, content_type='application/json')


@app.route('/live', methods=['GET'])
def live():
    app.logger.info("Application status OK")
    return Response('{"status": "OK"}', status=200, content_type='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

