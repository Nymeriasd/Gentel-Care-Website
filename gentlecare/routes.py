from gentlecare import app, db
from flask import redirect, url_for, render_template, request, make_response
import urllib3, json, requests, calendar, random, string
from datetime import datetime
from gentlecare.models import Service ,Farmer, Business, Price, Situation, OrdersMaintenance, OrderStatus, Priority, ExtraService, Time
from datetime import timedelta


response = ""

def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# index route 
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

# contactus route 
@app.route('/contactus', methods=['GET','POST'])
def contactus():
    if request.method == 'POST':
        try :
            msg = Message(request.form['form-subject'], sender='contact@example.com', recipients=['your_email@example.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (request.form['form-name'], request.form['form-email'], request.form['form-message'])
            mail.send(msg)
        except Exception as err :
            return render_template('contactus.html')
    elif request.method == 'GET' :
        return render_template('contactus.html')

# aboutus route 
@app.route('/aboutus', methods=['GET','POST'])
def aboutus():
    return render_template('aboutus.html')

# ourservices route 
@app.route('/ourservices', methods=['GET','POST'])
def ourservices():
    return render_template('ourservices.html')


# maintenance route 
@app.route('/maintenance', methods=['GET','POST'])
def maintenance():
    ServiceItems  = db.session.query(Service).join(Situation).filter(Situation.Situation == 'Enabled').all()
    PriorityItems = db.session.query(Priority).all()
    TimeItems = db.session.query(Time).all()
    return render_template('maintenance.html', ServiceItems = ServiceItems, PriorityItems = PriorityItems, TimeItems = TimeItems)
  

# cleaning route 
@app.route('/cleaning', methods=['GET','POST'])
def cleaning():
    ExtraServiceItems = db.session.query(ExtraService).join(Situation).filter(Situation.Situation == 'Enabled').all()
    return render_template('cleaning.html', ExtraServiceItems = ExtraServiceItems)


# checkout route 
@app.route('/checkout', methods=['GET','POST'])
def checkout():
    if request.method == "POST" :
        IdService = request.form.get('Service')
        IdPriority = request.form.get('Priority')
        Orderdate = request.form.get('Orderdate')
        time = request.form.get('time')
        comments = request.form.get('comment')

        GetService = db.session.query(Service).filter_by(IdService = IdService).one()
        GetPriority = db.session.query(Priority).filter_by(IdPriority = IdPriority).one()

        return render_template('checkout.html' , Service = GetService , Priority = GetPriority , Orderdate = Orderdate , time = time , comments = comments)
        

# add Order route 
@app.route('/checkout/<int:IdService>/<int:IdPriority>/<float:Price>/<Orderdate>/<Time>/<Comment>/add', methods=['GET','POST'])
def addOrder(IdService,IdPriority,Price,Orderdate,Time,Comment):
    if request.method == "POST" :
        NewOrder = OrdersMaintenance(OrderNumber = "O"+random_string_generator(), FirstName = request.form.get('fname'), LastName = request.form.get('lname'), PhoneNumber = request.form.get('phone'), Email = request.form.get('email'), Address = request.form.get('address'), IdService =  IdService, IdOrderStatus = 1, Price = Price, IdPriority = IdPriority, Ordertime = Orderdate, Time = Time, Comment = Comment)
        try :
            db.session.add(NewOrder)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as err :
            return redirect(url_for('index'))
