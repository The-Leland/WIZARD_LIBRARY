


from flask import jsonify
from models.spell import Spell
from db import db

def create_spell(data):
    try:
        spell = Spell(
            spell_name=data['spell_name'],
            incantation=data.get('incantation'),
            difficulty_level=data.get('difficulty_level'),
            spell_type=data.get('spell_type'),
            description=data.get('description')
        )
        db.session.add(spell)
        db.session.commit()
        return jsonify(message="Spell created successfully", spell_id=str(spell.spell_id)), 201
    except Exception as e:
        return jsonify(error=str(e)), 400


def get_all_spells():
    spells = Spell.query.all()
    return jsonify([
        {
            "spell_id": str(s.spell_id),
            "spell_name": s.spell_name,
            "incantation": s.incantation,
            "difficulty_level": s.difficulty_level,
            "spell_type": s.spell_type,
            "description": s.description
        }
        for s in spells
    ]), 200


def get_spells_by_difficulty(difficulty_level):
    spells = Spell.query.filter_by(difficulty_level=difficulty_level).all()
    return jsonify([
        {
            "spell_id": str(s.spell_id),
            "spell_name": s.spell_name,
            "difficulty_level": s.difficulty_level
        }
        for s in spells
    ]), 200


def get_spell_by_id(spell_id):
    spell = Spell.query.get(spell_id)
    if not spell:
        return jsonify(error="Spell not found"), 404

    return jsonify({
        "spell_id": str(spell.spell_id),
        "spell_name": spell.spell_name,
        "incantation": spell.incantation,
        "difficulty_level": spell.difficulty_level,
        "spell_type": spell.spell_type,
        "description": spell.description
    }), 200


def update_spell(spell_id, data):
    spell = Spell.query.get(spell_id)
    if not spell:
        return jsonify(error="Spell not found"), 404

    for key, value in data.items():
        setattr(spell, key, value)

    db.session.commit()
    return jsonify(message="Spell updated successfully"), 200


def delete_spell(spell_id):
    spell = Spell.query.get(spell_id)
    if not spell:
        return jsonify(error="Spell not found"), 404

    db.session.delete(spell)
    db.session.commit()
    return jsonify(message="Spell deleted successfully"), 200