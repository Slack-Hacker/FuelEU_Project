from flask import Blueprint, jsonify
from app.models import Vessel

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to FuelEU Maritime Backend!"})

@main.route('/vessels', methods=['GET'])
def get_vessels():
    vessels = Vessel.query.all()
    data = [{"id": v.id, "name": v.name, "fuel_type": v.fuel_type, "emissions": v.emissions} for v in vessels]
    return jsonify(data)
