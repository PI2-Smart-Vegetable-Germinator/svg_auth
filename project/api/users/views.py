from flask import Blueprint
from flask import jsonify
from flask import request

from project import db
from project.api.auth.models import Users

from .schemas import UsersSchema


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/api/users', methods=['GET'])
def get_users():
    schema = UsersSchema()

    users = Users.query.all()

    return jsonify({
        'users': [schema.dump(user) for user in users]
    }), 200



@users_blueprint.route('/api/users/<int:id>', methods=['GET'])
def get_single_user(id):
    schema = UsersSchema()

    user = Users.query.filter_by(id=id).first()

    return jsonify({
        'user': schema.dump(user)
    }), 200


@users_blueprint.route('/api/pairing', methods=['PUT'])
def pair_user_to_machine():
    put_data = request.get_json()

    user_id = put_data['userId']
    machine_id = put_data['machineId']

    user = Users.query.filter_by(id=user_id).first()
    user.machine_id = machine_id

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success': True

@users_blueprint.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):

    user = Users.query.filter_by(id=int(user_id)).first()

    return jsonify({
        'email': user.email,
        'deviceId': user.device_id,
        'machineId': user.machine_id

    }), 200
