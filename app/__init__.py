from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')
    db.init_app(app)
    migrate = Migrate(app, db)

    
    from app.routes.main import main
    from app.routes.vessels import vessels_bp
    from app.routes.fuels import fuels_bp
    from app.routes.compliance import compliance_bp
    
    app.register_blueprint(main)
    app.register_blueprint(vessels_bp)
    app.register_blueprint(fuels_bp)
    app.register_blueprint(compliance_bp)


    return app
