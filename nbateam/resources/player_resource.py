from flask_restful import Resource
from marshmallow import fields, Schema

from nbateam.models import Player


class PlayerInfoSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    display_first_last = fields.String()
    display_last_comma_first = fields.String()
    display_fi_last = fields.String()
    birthdate = fields.DateTime()
    school = fields.String()
    country = fields.String()
    last_affiliation = fields.String()
    height = fields.String()
    weight = fields.Integer()
    season_exp = fields.Integer()
    jersey = fields.Integer()
    position = fields.String()
    roster_status = fields.String()
    team_id = fields.Integer()
    team_city = fields.String()
    team_name = fields.String()
    team_abbrev = fields.String()
    team_code = fields.String()
    player_code = fields.String()
    from_year = fields.Integer()
    to_year = fields.Integer()
    has_played_dleague = fields.Boolean()
    has_games_played = fields.Boolean()
    draft_year = fields.Integer()
    draft_round = fields.Integer()
    draft_number = fields.Integer()

    class Meta:
        ordered = True


class PlayerCareerStatsSchema(Schema):
    is_postseason = fields.Boolean()
    gp = fields.Integer()
    gs = fields.Integer()
    min = fields.Integer()
    fgm = fields.Integer()
    fga = fields.Integer()
    fg_pct = fields.Float()
    fg3m = fields.Integer()
    fg3a = fields.Integer()
    fg3_pct = fields.Float()
    ftm = fields.Integer()
    fta = fields.Integer()
    ft_pct = fields.Integer()
    oreb = fields.Integer()
    dreb = fields.Integer()
    reb = fields.Integer()
    ast = fields.Integer()
    stl = fields.Integer()
    blk = fields.Integer()
    tov = fields.Integer()
    pf = fields.Integer()
    pts = fields.Integer()

    class Meta:
        ordered = True


class PlayerSeasonStatsSchema(Schema):
    is_postseason = fields.Boolean()
    season_id = fields.String()
    team_id = fields.Integer()
    team_abbrev = fields.String()
    player_age = fields.Integer()
    gp = fields.Integer()
    gs = fields.Integer()
    min = fields.Integer()
    fgm = fields.Integer()
    fga = fields.Integer()
    fg_pct = fields.Float()
    fg3m = fields.Integer()
    fg3a = fields.Integer()
    fg3_pct = fields.Float()
    ftm = fields.Integer()
    fta = fields.Integer()
    ft_pct = fields.Integer()
    oreb = fields.Integer()
    dreb = fields.Integer()
    reb = fields.Integer()
    ast = fields.Integer()
    stl = fields.Integer()
    blk = fields.Integer()
    tov = fields.Integer()
    pf = fields.Integer()
    pts = fields.Integer()

    class Meta:
        ordered = True


class PlayerSchema(Schema):
    id = fields.Integer()
    display_name = fields.String()
    roster_status = fields.Boolean()
    player_info = fields.Nested(PlayerInfoSchema)
    career_totals_regular_season = fields.Nested(PlayerCareerStatsSchema)
    career_totals_postseason = fields.Nested(PlayerCareerStatsSchema)
    season_totals_regular_season = fields.Nested(PlayerSeasonStatsSchema, many=True)
    season_totals_postseason = fields.Nested(PlayerSeasonStatsSchema, many=True)

    class Meta:
        ordered = True


class PlayerDetail(Resource):

    schema = PlayerSchema()

    def get(self, player_id):
        player = Player.query.get_or_404(player_id)
        return self.schema.dump(player)
