from flask import Flask
from app.database import db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.sqlite3"
app.config["UPLOAD_FOLDER"]='Uploads'
app.config['STATIC_FOLDER'] = 'Static'

db.init_app(app)
app.app_context().push()

from app.controllers import *

app.run(debug=True)