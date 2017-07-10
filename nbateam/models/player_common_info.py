from nbateam.extensions import db


class PlayerCommonInfo(db.Model):
    __tablename__ = 'player_common_info'

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, index=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    display_first_last = db.Column(db.String, nullable=False)
    display_last_comma_first = db.Column(db.String, nullable=False)
    display_fi_last = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    school = db.Column(db.String)
    country = db.Column(db.String)
    last_affiliation = db.Column(db.String)
    height = db.Column(db.String)
    weight = db.Column(db.Integer)
    season_exp = db.Column(db.Integer, nullable=False)
    jersey = db.Column(db.Integer)
    position = db.Column(db.String)
    roster_status = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer)
    team_city = db.Column(db.String)
    team_name = db.Column(db.String)
    team_abbrev = db.Column(db.String)
    team_code = db.Column(db.String)
    player_code = db.Column(db.String)
    from_year = db.Column(db.Integer, nullable=False)
    to_year = db.Column(db.Integer, nullable=False)
    has_played_dleague = db.Column(db.Boolean, nullable=False)
    has_games_played = db.Column(db.Boolean, nullable=False)
    draft_year = db.Column(db.Integer)
    draft_round = db.Column(db.Integer)
    draft_number = db.Column(db.Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Player Common Info %d>' % self.player_id
