from flask import Blueprint, request, jsonify
from app import db
from app.models import FuelRecord, Vessel

fuels_bp = Blueprint('fuels', __name__)

@fuels_bp.route('/fuels', methods=['POST'])
def add_fuel_record():
    data = request.get_json()
    vessel_id = data.get("vessel_id")
    fuel_type = data.get("fuel_type")
    amount = data.get("amount")
    emission_factor = data.get("emission_factor")

    if not all([vessel_id, fuel_type, amount, emission_factor]):
        return jsonify({"error": "Missing required fields"}), 400

    total_emission = amount * emission_factor
    record = FuelRecord(
        vessel_id=vessel_id,
        fuel_type=fuel_type,
        amount=amount,
        emission_factor=emission_factor,
        total_emission=total_emission
    )

    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Fuel record added", "total_emission": total_emission}), 201


@fuels_bp.route('/fuels/<int:vessel_id>', methods=['GET'])
def get_vessel_fuel_records(vessel_id):
    records = FuelRecord.query.filter_by(vessel_id=vessel_id).all()
    data = [
        {
            "id": r.id,
            "fuel_type": r.fuel_type,
            "amount": r.amount,
            "emission_factor": r.emission_factor,
            "total_emission": r.total_emission
        }
        for r in records
    ]
    return jsonify(data)
