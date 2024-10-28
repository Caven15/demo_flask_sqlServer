from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données
    server = 'localhost'
    database = 'MaBaseDeDonnees'
    driver = 'ODBC Driver 17 for SQL Server'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation de l'extension
    db.init_app(app)

    # Enregistrement des routes
    from app.route import main  # Importation du blueprint
    app.register_blueprint(main)

    return app
