from bottle import Bottle, run, route, static_file, request, response, template, redirect, get, post
from pymongo import MongoClient
from passlib.context import CryptContext
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
    
@app.get('/login') # or @route('/login')
def login():
    return static_file('login.html', root='templates/')

@app.post('/login')
def login():
    username = request.forms.get('uname')
    password = request.forms.get('psw')

    hashpass1 = hl.sha256(password).hexdigest()

    print(hashpass1)
    
    cur = db.signupTable.find({'Username': username})
    data = json.loads(dumps(cur))
    
    if(len(data) != 0):
        if(data[0]["Password"] == hashpass1):
            return {'status': 'User authenticated!', 'uname': username}
            print(hashpass1)
        else:
            return {'status': 'Invalid credentials'}
            print(hashpass1)
    else:
        return {'status': "User dosen't exist"}
        print(hashpass1)
    
# run(host='localhost', port=8081)