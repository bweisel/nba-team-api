from flask import Blueprint, jsonify
from flask_restful import Api

from nbateam.common.exceptions import SchemaValidationError
from nbateam.resources import UserDetail, UserList, PlayerDetail


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

api.add_resource(UserDetail, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(PlayerDetail, '/players/<int:player_id>')


@api_bp.errorhandler(SchemaValidationError)
def handle_invalid_schema(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
