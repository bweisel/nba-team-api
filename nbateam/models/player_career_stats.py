from nbateam.extensions import db


class PlayerCareerStats(db.Model):
    __tablename__ = 'player_career_stats'

    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True, index=True)
    is_postseason = db.Column(db.Boolean, primary_key=True, nullable=False)
    gp = db.Column(db.Integer, nullable=False)
    gs = db.Column(db.Integer, nullable=False)
    min = db.Column(db.Integer, nullable=False)
    fgm = db.Column(db.Integer, nullable=False)
    fga = db.Column(db.Integer, nullable=False)
    fg_pct = db.Column(db.Float, nullable=False)
    fg3m = db.Column(db.Integer, nullable=False)
    fg3a = db.Column(db.Integer, nullable=False)
    fg3_pct = db.Column(db.Float, nullable=False)
    ftm = db.Column(db.Integer, nullable=False)
    fta = db.Column(db.Integer, nullable=False)
    ft_pct = db.Column(db.Float, nullable=False)
    oreb = db.Column(db.Integer, nullable=False)
    dreb = db.Column(db.Integer, nullable=False)
    reb = db.Column(db.Integer, nullable=False)
    ast = db.Column(db.Integer, nullable=False)
    stl = db.Column(db.Integer, nullable=False)
    blk = db.Column(db.Integer, nullable=False)
    tov = db.Column(db.Integer, nullable=False)
    pf = db.Column(db.Integer, nullable=False)
    pts = db.Column(db.Integer, nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Player Career Stats %d>' % self.gp
