


from flask import Blueprint, request
from controllers.spells_controller import (
    create_spell,
    get_all_spells,
    get_spells_by_difficulty,
    get_spell_by_id,
    update_spell,
    delete_spell
)

spells_routes = Blueprint('spells_routes', __name__)

@spells_routes.route('/spell', methods=['POST'])
def create():
    return create_spell(request.json)

@spells_routes.route('/spells', methods=['GET'])
def get_all():
    return get_all_spells()

@spells_routes.route('/spells/<float:difficulty_level>', methods=['GET'])
def get_by_difficulty(difficulty_level):
    return get_spells_by_difficulty(difficulty_level)

@spells_routes.route('/spell/<spell_id>', methods=['GET'])
def get_by_id(spell_id):
    return get_spell_by_id(spell_id)

@spells_routes.route('/spell/<spell_id>', methods=['PUT'])
def update(spell_id):
    return update_spell(spell_id, request.json)

@spells_routes.route('/spell/delete/<spell_id>', methods=['DELETE'])
def delete(spell_id):
    return delete_spell(spell_id)
