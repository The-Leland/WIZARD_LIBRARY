

from flask import jsonify
from models.wizard_specialization import WizardSpecialization
from db import db
from datetime import datetime

def create_specialization_entry(data):
    try:
        specialization = WizardSpecialization(
            wizard_id=data['wizard_id'],
            spell_id=data['spell_id'],
            proficiency_level=data.get('proficiency_level'),
            date_learned=datetime.strptime(data['date_learned'], "%Y-%m-%d")
        )
        db.session.add(specialization)
        db.session.commit()
        return jsonify(message="Specialization created successfully"), 201
    except Exception as e:
        return jsonify(error=str(e)), 400
    


def get_spells_for_wizard(wizard_id):
    specializations = WizardSpecialization.query.filter_by(wizard_id=wizard_id).all()
    return jsonify([
        {
            "spell_id": str(s.spell_id),
            "proficiency_level": s.proficiency_level,
            "date_learned": s.date_learned.strftime("%Y-%m-%d")
        }
        for s in specializations
    ]), 200


def get_wizards_for_spell(spell_id):
    specializations = WizardSpecialization.query.filter_by(spell_id=spell_id).all()
    return jsonify([
        {
            "wizard_id": str(s.wizard_id),
            "proficiency_level": s.proficiency_level,
            "date_learned": s.date_learned.strftime("%Y-%m-%d")
        }
        for s in specializations
    ]), 200


def update_specialization(wizard_id, spell_id, data):
    specialization = WizardSpecialization.query.get((wizard_id, spell_id))
    if not specialization:
        return jsonify(error="Specialization not found"), 404

    for key, value in data.items():
        setattr(specialization, key, value)

    db.session.commit()
    return jsonify(message="Specialization updated successfully"), 200

def delete_specialization(wizard_id, spell_id):
    specialization = WizardSpecialization.query.get((wizard_id, spell_id))
    if not specialization:
        return jsonify(error="Specialization not found"), 404

    db.session.delete(specialization)
    db.session.commit()
    return jsonify(message="Specialization deleted successfully"), 200
    
def get_all_specializations():
    specializations = WizardSpecialization.query.all()
    return jsonify([
        {
            "wizard_id": str(s.wizard_id),
            "spell_id": str(s.spell_id),
            "proficiency_level": s.proficiency_level,
            "date_learned": s.date_learned.strftime("%Y-%m-%d")
        }
        for s in specializations
    ]), 200
