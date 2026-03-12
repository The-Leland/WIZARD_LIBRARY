from flask import jsonify
from models.school import School
from db import db

def create_school(data):
    try:
        school = School(
            school_name=data['school_name'],
            location=data.get('location'),
            founded_year=data.get('founded_year'),
            headmaster=data.get('headmaster')
        )
        db.session.add(school)
        db.session.commit()
        return jsonify(message="School created successfully", school_id=str(school.school_id)), 201
    except Exception as e:
        return jsonify(error=str(e)), 400


def get_all_schools():
    schools = School.query.all()
    return jsonify([
        {
            "school_id": str(s.school_id),
            "school_name": s.school_name,
            "location": s.location,
            "founded_year": s.founded_year,
            "headmaster": s.headmaster
        }
        for s in schools
    ]), 200


def get_school_by_id(school_id):
    school = School.query.get(school_id)
    if not school:
        return jsonify(error="School not found"), 404

    return jsonify({
        "school_id": str(school.school_id),
        "school_name": school.school_name,
        "location": school.location,
        "founded_year": school.founded_year,
        "headmaster": school.headmaster
    }), 200


def update_school(school_id, data):
    school = School.query.get(school_id)
    if not school:
        return jsonify(error="School not found"), 404

    for key, value in data.items():
        setattr(school, key, value)

    db.session.commit()
    return jsonify(message="School updated successfully"), 200


def delete_school(school_id):
    school = School.query.get(school_id)
    if not school:
        return jsonify(error="School not found"), 404

    db.session.delete(school)
    db.session.commit()
    return jsonify(message="School deleted successfully"), 200