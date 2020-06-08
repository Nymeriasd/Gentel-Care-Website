from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_mail import Message, Mail


app = Flask(__name__, static_folder = 'static', template_folder='templates')
app.config['SECRET_KEY'] = 'gentlecare'
socket_location = "/var/run/mysqld/mysqld.sock"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/gentlecare"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@178.62.66.6/gentlecare"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'
 
mail = Mail(app)
db = SQLAlchemy(app)
from gentlecare import routes