

from flask import Blueprint, request
from controllers.wizards_controller import (
    create_wizard,
    get_all_wizards,
    get_active_wizards,
    get_wizards_by_house,
    get_wizards_by_power,
    get_wizard_by_id,
    update_wizard,
    delete_wizard
)

wizards_routes = Blueprint('wizards_routes', __name__)

@wizards_routes.route('/wizard', methods=['POST'])
def create():
    return create_wizard(request.json)

@wizards_routes.route('/wizards', methods=['GET'])
def get_all():
    return get_all_wizards()

@wizards_routes.route('/wizards/active', methods=['GET'])
def get_active():
    return get_active_wizards()

@wizards_routes.route('/wizards/<house>', methods=['GET'])
def get_by_house(house):
    return get_wizards_by_house(house)

@wizards_routes.route('/wizards/power/<int:magical_power_level>', methods=['GET'])
def get_by_power(magical_power_level):
    return get_wizards_by_power(magical_power_level)

@wizards_routes.route('/wizard/<wizard_id>', methods=['GET'])
def get_by_id(wizard_id):
    return get_wizard_by_id(wizard_id)

@wizards_routes.route('/wizard/<wizard_id>', methods=['PUT'])
def update(wizard_id):
    return update_wizard(wizard_id, request.json)

@wizards_routes.route('/wizard/delete/<wizard_id>', methods=['DELETE'])
def delete(wizard_id):
    return delete_wizard(wizard_id)

