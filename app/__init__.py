from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize database
    db.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
