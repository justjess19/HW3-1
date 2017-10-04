## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the 
#README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)


@app.route('/artistinfo')
def artist_info():
    return render_template('artist_info.html')

@app.route('/artistlinks')
def artistlinks():
    return render_template('artist_links.html')

#artistform.html`
#* `http://localhost:5000/artistinfo` -> `artist_info.html`
#* `http://localhost:5000/artistlinks` -> `artist_links.html`
#* `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`