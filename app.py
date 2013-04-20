"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import requests, csv, StringIO
import json
app = Flask(__name__)

gdoc_template = "https://docs.google.com/spreadsheet/pub?key={0}&output=csv"

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.after_request
def after(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/<key>/')
def home(key):
    """Render website's home page."""
    results = []

    resp = requests.get(gdoc_template.format(key)) 
    if resp.ok:
        sio = StringIO.StringIO(resp.content)
        dr = csv.DictReader(sio)
        for row in dr:
            results.append(row)
   
    return Response(response=json.dumps(results), 
            status=200, 
            mimetype='application/json')



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
