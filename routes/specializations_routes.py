

from flask import Blueprint, request
from controllers.specializations_controller import (
    create_specialization_entry,
    get_spells_for_wizard,
    get_wizards_for_spell,
    update_specialization,
    delete_specialization,
    get_all_specializations
)

specializations_routes = Blueprint('specializations_routes', __name__)

@specializations_routes.route('/wizard/specialize', methods=['POST'])
def create_specialization():
    return create_specialization_entry(request.json)

@specializations_routes.route('/specializations', methods=['GET'])
def get_all():
    return get_all_specializations()

@specializations_routes.route('/wizard/<wizard_id>/spells', methods=['GET'])
def get_wizard_spells(wizard_id):
    return get_spells_for_wizard(wizard_id)

@specializations_routes.route('/spell/<spell_id>/wizards', methods=['GET'])
def get_spell_wizards(spell_id):
    return get_wizards_for_spell(spell_id)

@specializations_routes.route('/wizard/<wizard_id>/spell/<spell_id>', methods=['PUT'])
def update_specialization_route(wizard_id, spell_id):
    return update_specialization(wizard_id, spell_id, request.json)

@specializations_routes.route('/wizard/<wizard_id>/spell/<spell_id>', methods=['DELETE'])
def delete_specialization_route(wizard_id, spell_id):
    return delete_specialization(wizard_id, spell_id)