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
