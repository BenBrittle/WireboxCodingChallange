from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

from app import db, app
with app.app_context():
    db.create_all()
