from nbateam.extensions import db
from sqlalchemy.orm import relationship


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer, nullable=False)
    display_name = db.Column(db.String, nullable=False)
    roster_status = db.Column(db.Boolean, nullable=False)
    from_year = db.Column(db.Integer, nullable=False)
    to_year = db.Column(db.Integer, nullable=False)
    player_code = db.Column(db.String)
    team_id = db.Column(db.Integer)
    team_city = db.Column(db.String)
    team_name = db.Column(db.String)
    team_abbrev = db.Column(db.String)
    team_code = db.Column(db.String)
    has_games_played = db.Column(db.Boolean, nullable=False)

    player_info = \
        relationship('PlayerCommonInfo',
                     primaryjoin='and_(Player.id==PlayerCommonInfo.player_id)',
                     uselist=False)

    career_totals_regular_season = \
        relationship('PlayerCareerStats',
                     primaryjoin='and_(Player.id==PlayerCareerStats.player_id, '
                                 'PlayerCareerStats.is_postseason==False)',
                     uselist=False)
    career_totals_postseason = \
        relationship('PlayerCareerStats',
                     primaryjoin='and_(Player.id==PlayerCareerStats.player_id, '
                                 'PlayerCareerStats.is_postseason==True)',
                     uselist=False)
    season_totals_regular_season = \
        relationship('PlayerSeasonStats',
                     primaryjoin='and_(Player.id==PlayerSeasonStats.player_id, '
                                 'PlayerSeasonStats.is_postseason==False)',
                     order_by='PlayerSeasonStats.season_id',
                     uselist=True)
    season_totals_postseason = \
        relationship('PlayerSeasonStats',
                     primaryjoin='and_(Player.id==PlayerSeasonStats.player_id, '
                                 'PlayerSeasonStats.is_postseason==True)',
                     order_by='PlayerSeasonStats.season_id',
                     uselist=True)

    def __init__(self):
        pass

    # def __repr__(self):
    #     return '<Player %d>' % self.id
