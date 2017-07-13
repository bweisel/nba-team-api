from flask import request
from flask_restful import Resource

from nbateam.common.schema_utils import BaseAPISchema
from nbateam.extensions import db
from nbateam.models import UserTeam


class UserTeamSchema(BaseAPISchema):

    class Meta:
        model = UserTeam
        include_fk = True


class UserTeamList(Resource):

    db_schema = UserTeamSchema()
    response_schema = UserTeamSchema(many=True)

    def post(self):
        print(request.headers['Authorization'])

        try:
            db_team = self.db_schema.load(request.get_json())
            db.session.add(db_team)
            db.session.commit()
            return self.db_schema.dump(db_team), 201
        except Exception as e:
            db.session.rollback()
            print(e)
            return str(e), 500

    def get(self):
        user_teams = UserTeam.query.all()
        results = self.response_schema.dump(user_teams)
        return results
