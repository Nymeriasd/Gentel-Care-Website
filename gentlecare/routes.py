from gentlecare import app, db
from flask import redirect, url_for, render_template, request, make_response
import urllib3, json, requests, calendar, random, string
from datetime import datetime
from gentlecare.models import Service,Farmer, Business, Price, Situation, Orders, OrderStatus
from datetime import timedelta


response = ""

def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# index route 
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

# maintenance route 
@app.route('/maintenance', methods=['GET','POST'])
def maintenance():
    return render_template('maintenance.html')


# cleaning route 
@app.route('/cleaning', methods=['GET','POST'])
def cleaning():
    return render_template('cleaning.html')