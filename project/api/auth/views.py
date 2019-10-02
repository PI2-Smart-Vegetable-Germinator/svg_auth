from flask import Blueprint
from flask import jsonify
from flask import request
from flask import url_for

from flask_bcrypt import generate_password_hash

from marshmallow.exceptions import ValidationError

from project import db
from .schemas import SignupSchema

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({
        'response': 'pong!'
    }), 200


@auth_blueprint.route('/api/signup', methods=['POST'])
def signup():
    post_data = request.get_json()
    schema = SignupSchema()

    try:
        user = schema.load(post_data.get('user'))
        user.password = generate_password_hash(user.password)
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success': True,
    }), 201
