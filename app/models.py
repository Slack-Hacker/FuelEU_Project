from app import db

class Vessel(db.Model):
    __tablename__ = 'vessels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    emissions = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Vessel {self.name}>'
    
class FuelRecord(db.Model):
    __tablename__ = 'fuel_records'
    id = db.Column(db.Integer, primary_key=True)
    vessel_id = db.Column(db.Integer, db.ForeignKey('vessels.id'), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    emission_factor = db.Column(db.Float, nullable=False)
    total_emission = db.Column(db.Float, nullable=False)

    vessel = db.relationship('Vessel', backref=db.backref('fuel_records', lazy=True))

