


from flask import Flask
from db import db
from routes.wizards_routes import wizards_routes
from routes.schools_routes import schools_routes
from routes.books_routes import books_routes
from routes.spells_routes import spells_routes
from routes.specializations_routes import specializations_routes
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(wizards_routes)
app.register_blueprint(schools_routes)
app.register_blueprint(books_routes)
app.register_blueprint(spells_routes)
app.register_blueprint(specializations_routes)

with app.app_context():
    from models.wizard import Wizard
    from models.school import School
    from models.book import Book
    from models.spell import Spell
    from models.wizard_specialization import WizardSpecialization
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    