from bottle import Bottle, run, route, static_file, request, response, template, redirect, get, post
from passlib.context import CryptContext
from pymongo import MongoClient
from bson.json_util import dumps
import json
import hashlib as hl

client = MongoClient()
db = client.signup

app = Bottle(__name__)

# Static Routes
@app.route('/<filename:re:.*\.html>')
def javascripts(filename):
    return static_file(filename, root='templates')

@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.html>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.pdf>')
def pdfs(filename):
    return static_file(filename, root='static')

@app.route('/<filename:re:.*\.json>')
def javascripts(filename):
    return static_file(filename, root='static')

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    
@app.get('/signup') # or @route('/login')
def signup():
    return static_file('signup.html', root='templates/')

@app.post('/signup')
def signup():
    fname = request.forms.get('fname')
    lname = request.forms.get('lname')
    username = request.forms.get('uname')
    password = hl.sha256(request.forms.get('psw')).hexdigest()
    email = request.forms.get('email')

    db.signupTable.insert_one({'First Name' : fname , 'Last Name' : lname , 'Username' : username , 'Password' : password , 'Email ID' : email})

    return "success"

# run(host='localhost', port=8081)