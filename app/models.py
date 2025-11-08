from app import db

class Vessel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    emissions = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Vessel {self.name}>'
