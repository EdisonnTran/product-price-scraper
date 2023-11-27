from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__, template_folder="../frontend")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

from models import Item

@app.route('/', methods=['GET', 'POST'])
def tracker():
    if (request.method == 'POST'):
        data = request.form.get("itemName")
        print(data)
    return render_template('tracker.html')


if __name__ == "__main__":
    app.run(debug=True)
