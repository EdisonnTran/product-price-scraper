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

            if ('delete' not in request.form.keys()):
                item = request.form.get("itemName")
                query = Item.query.filter_by(itemName=item).first()

                if (not query and item):
                    new_item = Item(itemName = item)
                    db.session.add(new_item)
                    db.session.commit()
                    print(f"{item} added!")

                else:
                    print(f"{item} is already on the list!")

            else:

                # Delete from list
                checklist = request.form.getlist("delList")
                for selected in checklist:
                    query = Item.query.filter_by(id = selected).first()
                    db.session.delete(query)
                    db.session.commit()
                    print(f"{query.itemName} Deleted!")

        items = Item.query.all()

        return render_template('tracker.html', items=items)
    
    return app


def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database file created')
