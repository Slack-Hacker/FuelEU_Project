from flask import Blueprint, request, jsonify
from app import db
from app.models import Vessel

vessels_bp = Blueprint('vessels', __name__)

# GET – list all vessels
@vessels_bp.route('/vessels', methods=['GET'])
def list_vessels():
    vessels = Vessel.query.all()
    data = [{"id": v.id, "name": v.name, "fuel_type": v.fuel_type, "emissions": v.emissions} for v in vessels]
    return jsonify(data)

# POST – add a new vessel
@vessels_bp.route('/vessels', methods=['POST'])
def add_vessel():
    data = request.get_json()
    name = data.get("name")
    fuel_type = data.get("fuel_type")
    emissions = data.get("emissions")
    if not name or not fuel_type or emissions is None:
        return jsonify({"error": "Missing required fields"}), 400
    new_vessel = Vessel(name=name, fuel_type=fuel_type, emissions=emissions)
    db.session.add(new_vessel)
    db.session.commit()
    return jsonify({"message": "Vessel added successfully"}), 201

# PUT – update vessel details
@vessels_bp.route('/vessels/<int:id>', methods=['PUT'])
def update_vessel(id):
    vessel = Vessel.query.get(id)
    if not vessel:
        return jsonify({"error": "Vessel not found"}), 404
    data = request.get_json()
    vessel.name = data.get("name", vessel.name)
    vessel.fuel_type = data.get("fuel_type", vessel.fuel_type)
    vessel.emissions = data.get("emissions", vessel.emissions)
    db.session.commit()
    return jsonify({"message": "Vessel updated successfully"})

# DELETE – remove a vessel
@vessels_bp.route('/vessels/<int:id>', methods=['DELETE'])
def delete_vessel(id):
    vessel = Vessel.query.get(id)
    if not vessel:
        return jsonify({"error": "Vessel not found"}), 404
    db.session.delete(vessel)
    db.session.commit()
    return jsonify({"message": "Vessel deleted successfully"})
