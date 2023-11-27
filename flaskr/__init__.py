from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .models import Item

    create_database(app)

    @app.route('/', methods=['GET', 'POST'])
    def tracker():
        if (request.method == 'POST'):
            data = request.form.get("itemName")
            print(data)
        return render_template('tracker.html')
    
    return app


def create_database(app):
    if not path.exists('flaskr/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database file created')