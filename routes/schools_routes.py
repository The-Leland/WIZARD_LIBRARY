

from flask import Blueprint, request
from controllers.schools_controller import (
    create_school,
    get_all_schools,
    get_school_by_id,
    update_school,
    delete_school
)

schools_routes = Blueprint('schools_routes', __name__)

@schools_routes.route('/school', methods=['POST'])
def create():
    return create_school(request.json)

@schools_routes.route('/schools', methods=['GET'])
def get_all():
    return get_all_schools()

@schools_routes.route('/school/<school_id>', methods=['GET'])
def get_by_id(school_id):
    return get_school_by_id(school_id)

@schools_routes.route('/school/<school_id>', methods=['PUT'])
def update(school_id):
    return update_school(school_id, request.json)

@schools_routes.route('/school/delete/<school_id>', methods=['DELETE'])
def delete(school_id):
    return delete_school(school_id)


