

from flask import jsonify
from models.wizard import Wizard
from db import db

def create_wizard(data):
    try:
        wizard = Wizard(
            school_id=data['school_id'],
            wizard_name=data['wizard_name'],
            house=data.get('house'),
            year_enrolled=data.get('year_enrolled'),
            magical_power_level=data.get('magical_power_level'),
            active=data.get('active', True)
        )
        db.session.add(wizard)
        db.session.commit()
        return jsonify(message="Wizard created successfully", wizard_id=str(wizard.wizard_id)), 201
    except Exception as e:
        return jsonify(error=str(e)), 400


def get_all_wizards():
    wizards = Wizard.query.all()
    return jsonify([
        {
            "wizard_id": str(w.wizard_id),
            "school_id": str(w.school_id),
            "wizard_name": w.wizard_name,
            "house": w.house,
            "year_enrolled": w.year_enrolled,
            "magical_power_level": w.magical_power_level,
            "active": w.active
        }
        for w in wizards
    ]), 200


def get_active_wizards():
    wizards = Wizard.query.filter_by(active=True).all()
    return jsonify([
        {
            "wizard_id": str(w.wizard_id),
            "wizard_name": w.wizard_name
        }
        for w in wizards
    ]), 200


def get_wizards_by_house(house):
    wizards = Wizard.query.filter_by(house=house).all()
    return jsonify([
        {
            "wizard_id": str(w.wizard_id),
            "wizard_name": w.wizard_name
        }
        for w in wizards
    ]), 200


def get_wizards_by_power(power):
    wizards = Wizard.query.filter_by(magical_power_level=power).all()
    return jsonify([
        {
            "wizard_id": str(w.wizard_id),
            "wizard_name": w.wizard_name
        }
        for w in wizards
    ]), 200


def get_wizard_by_id(wizard_id):
    wizard = Wizard.query.get(wizard_id)
    if not wizard:
        return jsonify(error="Wizard not found"), 404

    return jsonify({
        "wizard_id": str(wizard.wizard_id),
        "school_id": str(wizard.school_id),
        "wizard_name": wizard.wizard_name,
        "house": wizard.house,
        "year_enrolled": wizard.year_enrolled,
        "magical_power_level": wizard.magical_power_level,
        "active": wizard.active
    }), 200


def update_wizard(wizard_id, data):
    wizard = Wizard.query.get(wizard_id)
    if not wizard:
        return jsonify(error="Wizard not found"), 404

    for key, value in data.items():
        setattr(wizard, key, value)

    db.session.commit()
    return jsonify(message="Wizard updated successfully"), 200


def delete_wizard(wizard_id):
    wizard = Wizard.query.get(wizard_id)
    if not wizard:
        return jsonify(error="Wizard not found"), 404

    db.session.delete(wizard)
    db.session.commit()
    return jsonify(message="Wizard deleted successfully"), 200

