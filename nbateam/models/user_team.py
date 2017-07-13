from nbateam.extensions import db


class UserTeam(db.Model):
    __tablename__ = 'user_team'

    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    player1 = db.Column(db.Integer, nullable=False)
    player2 = db.Column(db.Integer, nullable=False)
    player3 = db.Column(db.Integer, nullable=False)
    player4 = db.Column(db.Integer, nullable=False)
    player5 = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    comments = db.Column(db.String, nullable=True)

    def __repr__(self):
        return ''.join([f'{key}:{val},' if key != '_sa_instance_state' else '' for key, val in self.__dict__.items()]).rstrip(',')
