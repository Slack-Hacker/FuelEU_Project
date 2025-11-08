from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')
    db.init_app(app)

    from app.routes.main import main
    from app.routes.vessels import vessels_bp
    app.register_blueprint(main)
    app.register_blueprint(vessels_bp)

    return app
