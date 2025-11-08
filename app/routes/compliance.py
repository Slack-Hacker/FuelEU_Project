from flask import Blueprint, request, jsonify
from app import db
from app.models import Vessel, FuelRecord

compliance_bp = Blueprint('compliance', __name__)

TARGET_INTENSITY = 89.3368  # gCO2e/MJ (2025 target)

@compliance_bp.route('/compliance/cb/<int:vessel_id>', methods=['GET'])
def compute_cb(vessel_id):
    vessel = Vessel.query.get(vessel_id)
    if not vessel:
        return jsonify({"error": "Vessel not found"}), 404

    # Sum total energy
    records = vessel.fuel_records
    if not records:
        return jsonify({"error": "No fuel records found"}), 404

    total_energy_mj = sum(r.amount * 41000 for r in records)  # MJ = t * 41,000
    total_emission = sum(r.total_emission for r in records)

    # Compliance Balance = (Target - Actual) * Energy
    cb = (TARGET_INTENSITY - (total_emission / total_energy_mj)) * total_energy_mj

    return jsonify({
        "vessel_id": vessel.id,
        "vessel_name": vessel.name,
        "total_energy_mj": total_energy_mj,
        "total_emission": total_emission,
        "compliance_balance": cb
    })
