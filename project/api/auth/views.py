from flask import Blueprint
from flask import jsonify
from flask import request
from flask import url_for

from flask_bcrypt import check_password_hash
from flask_bcrypt import generate_password_hash

from marshmallow.exceptions import ValidationError

from project import db
from .models import Users
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
        # We need to decode the hash before saving it because of encoding issues with postgres.
        user = schema.load(post_data.get('user'))
        user.password = generate_password_hash(user.password).decode('utf-8')
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success': True,
        'userId': user.id
    }), 201


@auth_blueprint.route('/api/login', methods=['POST'])
def login():
    post_data = request.get_json()

    user = Users.query.filter_by(email=post_data['email']).first()

    if user and check_password_hash(user.password, post_data['password']):
        if post_data.get('deviceId'):
            user.device_id = post_data['deviceId']
            db.session.add(user)
            db.session.commit()

        return jsonify({
            'success': True,
            'userId': user.id
        }), 201

    return jsonify({
        'success': False,
        'message': 'Invalid e-mail or password'
    }), 401
