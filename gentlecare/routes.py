from gentlecare import app, db
from flask import redirect, url_for, render_template, request, make_response
import urllib3, json, requests, calendar, random, string
from datetime import datetime
from gentlecare.models import Service ,Farmer, Business, Price, Situation, Orders, OrderStatus, Priority, ExtraService
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
    ServiceItems  = db.session.query(Service).join(Situation).filter(Situation.Situation == 'Enabled').all()
    PriorityItems = db.session.query(Priority).all()
    return render_template('maintenance.html', ServiceItems = ServiceItems, PriorityItems = PriorityItems)


# cleaning route 
@app.route('/cleaning', methods=['GET','POST'])
def cleaning():
    ExtraServiceItems = db.session.query(ExtraService).join(Situation).filter(Situation.Situation == 'Enabled').all()
    return render_template('cleaning.html', ExtraServiceItems = ExtraServiceItems)


# contactus route 
@app.route('/contactus', methods=['GET','POST'])
def contactus():
    return render_template('contactus.html')

# aboutus route 
@app.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')

# ourservices route 
@app.route('/ourservices', methods=['GET','POST'])
def ourservices():
    return render_template('ourservices.html')

# checkout route 
@app.route('/checkout', methods=['GET','POST'])
def checkout():
    return render_template('checkout.html')