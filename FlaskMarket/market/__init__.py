# Intialisation File

from flask import Flask, render_template, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)# built-in magic variable is where to locate resources such as templates and static files.

#with app.app_context():
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # URI-Uniform Resource Identifier is to identify file.
app.config['SECRET_KEY'] = 'da0d069201643d2df5585c84'
db = SQLAlchemy(app) # db is database instance
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app) 
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

# in python cmd we have to write this below code 
#>>> from market import app
#>>> from market.models import db

from market import routes

#below code is require to create above database market.db and it will create the database
# >>>from app import app, db
# >>>app.app_context().push()
# >>>db.create_all()

# >>>from market import Item
# >>>item1 = Item(name='Iphone 10', price=500, barcode='12354432', description='desc') #in this we dont have to define id, as id is primary key if we run code, id becomes 1.
# >>>db.session.add(item) # to add item in database
# >>>db.session.commit()
# >>>Item.query.all() # [<Item 1>]

'''
@app.route('/') # it is a decorator, which check what url it have to navigate
def hello_world():
    return '<h1>Hello World!</h1>'
'''
'''
@app.route('/aboutpage/<username>') # here username is projected to dynamic route
def about_page(username):
    return f'<h3>This page is about hello {username}!</h3>'
'''

#if __name__=='__main__':
#   app.run(debug=True)