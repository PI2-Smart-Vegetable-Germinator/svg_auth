from flask import Blueprint
from flask import request
from flask import jsonify

from marshmallow.exceptions import ValidationError

from .schemas import DeviceIdSchema

from project import db
from project.api.auth.models import Users

notifications_blueprint = Blueprint('notifications', __name__)


@notifications_blueprint.route('/api/device_id', methods=['POST'])
def set_device_id():
    post_data = request.get_json()
    schema = DeviceIdSchema()

    try:
        post_data = schema.load(post_data)
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    user = Users.query.filter_by(id=post_data['user_id']).first()
    user.device_id = post_data['device_id']

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success': True
    }), 201
