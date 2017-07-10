import os
import time
from datetime import datetime
from random import randint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from nbateam.models import Player, PlayerCommonInfo, PlayerCareerStats, PlayerSeasonStats
from nbateam.scripts import nba_api_facade

# Initialize a DB connection
some_engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=some_engine)
session = Session()


def run():
    # Process any new players
    print('Checking for new players...')
    for player in nba_api_facade.get_all_players():
        player_external_id = player[0]

        db_player = session.query(Player).filter_by(external_id=player_external_id).first()
        if not db_player:
            print('Adding new player with external ID:', player_external_id)
            new_player_id = add_player(player)
            add_player_info(nba_api_facade.get_player_info(player_external_id), new_player_id)
            add_player_stats(nba_api_facade.get_player_stats(player_external_id), new_player_id)
            print('Done adding all data for player with external ID:', player_external_id)
            time.sleep(randint(1, 8))

    print('Done processing new players\n')

    # Update stats for active players
    print('Updating info for active players...')
    for player in session.query(Player).filter_by(to_year=2017).all():  #TODO make year dynamic
        # nba_api_facade.get_player_info(player.external_id)
        # nba_api_facade.get_player_stats(player.external_id)
        # add a new season if needed
        # update current season's stats
        pass

    print('Done updating stats')


def add_player(player_to_add):
    new_player = Player()
    new_player.external_id = player_to_add[0]
    new_player.display_name = player_to_add[2]
    new_player.roster_status = True if player_to_add[3] == 1 else False
    new_player.from_year = player_to_add[4]
    new_player.to_year = player_to_add[5]
    new_player.player_code = player_to_add[6]
    new_player.team_id = player_to_add[7]
    new_player.team_city = player_to_add[8]
    new_player.team_name = player_to_add[9]
    new_player.team_abbrev = player_to_add[10]
    new_player.team_code = player_to_add[11]
    new_player.has_games_played = player_to_add[12]

    try:
        session.add(new_player)
        session.commit()
        session.flush()
        print('Added player ID:', new_player.id)
        return new_player.id
    except Exception as e:
        print('Error adding new player!', e)


def add_player_info(player_info_to_add, internal_player_id):
    new_player_info = PlayerCommonInfo()
    new_player_info.player_id = internal_player_id
    new_player_info.first_name = player_info_to_add[1]
    new_player_info.last_name = player_info_to_add[2]
    new_player_info.display_first_last = player_info_to_add[3]
    new_player_info.display_last_comma_first = player_info_to_add[4]
    new_player_info.display_fi_last = player_info_to_add[5]
    new_player_info.birthdate = datetime.strptime(player_info_to_add[6], '%Y-%m-%dT%H:%M:%S')  # 1989-08-26T00:00:00
    new_player_info.school = player_info_to_add[7]
    new_player_info.country = handle_empty_strings(player_info_to_add[8])
    new_player_info.last_affiliation = player_info_to_add[9]
    new_player_info.height = handle_empty_strings(player_info_to_add[10])
    new_player_info.weight = int(player_info_to_add[11]) if (player_info_to_add[11] is not None and player_info_to_add[11].strip() != '') else None
    new_player_info.season_exp = player_info_to_add[12]
    new_player_info.jersey = handle_jersey(player_info_to_add[13])
    new_player_info.position = handle_empty_strings(player_info_to_add[14])
    new_player_info.roster_status = player_info_to_add[15]
    new_player_info.team_id = player_info_to_add[16]
    new_player_info.team_name = handle_empty_strings(player_info_to_add[17])
    new_player_info.team_abbrev = handle_empty_strings(player_info_to_add[18])
    new_player_info.team_code = handle_empty_strings(player_info_to_add[19])
    new_player_info.team_city = handle_empty_strings(player_info_to_add[20])
    new_player_info.player_code = player_info_to_add[21]
    new_player_info.from_year = player_info_to_add[22]
    new_player_info.to_year = player_info_to_add[23]
    new_player_info.has_played_dleague = player_info_to_add[24]
    new_player_info.has_games_played = player_info_to_add[25]
    new_player_info.draft_year = handle_undrafted(player_info_to_add[26])
    new_player_info.draft_round = handle_undrafted(player_info_to_add[27])
    new_player_info.draft_number = handle_undrafted(player_info_to_add[28])

    try:
        session.add(new_player_info)
        session.commit()
        print('Added player info for ID:', internal_player_id)
    except Exception as e:
        print('Error adding new player info!', e)


def add_player_stats(player_stats_to_add, internal_player_id):
    # career season totals (regular season)
    for row in player_stats_to_add[0]['rowSet']:
        session.add(build_season_stats_row(internal_player_id, row, False))

    # career totals (regular season)
    for row in player_stats_to_add[1]['rowSet']:

        session.add(build_career_stats_row(internal_player_id, row, False))

    # career season totals (postseason)
    for row in player_stats_to_add[2]['rowSet']:
        session.add(build_season_stats_row(internal_player_id, row, True))

    # career totals (postseason)
    for row in player_stats_to_add[3]['rowSet']:
        session.add(build_career_stats_row(internal_player_id, row, True))

    try:
        session.commit()
        print('Stats added for player ID', internal_player_id)
    except Exception as e:
        print('Error adding new player stats!', e)


def handle_none(param):
    return param if param is not None else 0


def build_season_stats_row(internal_player_id, row, is_postseason):
    to_return = PlayerSeasonStats()
    to_return.player_id = internal_player_id
    to_return.is_postseason = is_postseason
    to_return.season_id = handle_none(row[1])
    to_return.team_id = handle_none(row[3])
    to_return.team_abbrev = handle_none(row[4])
    to_return.player_age = int(handle_none(row[5]))
    to_return.gp = handle_none(row[6])
    to_return.gs = handle_none(row[7])
    to_return.min = handle_none(row[8])
    to_return.fgm = handle_none(row[9])
    to_return.fga = handle_none(row[10])
    to_return.fg_pct = handle_none(row[11])
    to_return.fg3m = handle_none(row[12])
    to_return.fg3a = handle_none(row[13])
    to_return.fg3_pct = handle_none(row[14])
    to_return.ftm = handle_none(row[15])
    to_return.fta = handle_none(row[16])
    to_return.ft_pct = handle_none(row[17])
    to_return.oreb = handle_none(row[18])
    to_return.dreb = handle_none(row[19])
    to_return.reb = handle_none(row[20])
    to_return.ast = handle_none(row[21])
    to_return.stl = handle_none(row[22])
    to_return.blk = handle_none(row[23])
    to_return.tov = handle_none(row[24])
    to_return.pf = handle_none(row[25])
    to_return.pts = handle_none(row[26])
    return to_return


def build_career_stats_row(internal_player_id, row, is_postseason):
    to_return = PlayerCareerStats()
    to_return.player_id = internal_player_id
    to_return.is_postseason = is_postseason
    to_return.gp = handle_none(row[3])
    to_return.gs = handle_none(row[4])
    to_return.min = handle_none(row[5])
    to_return.fgm = handle_none(row[6])
    to_return.fga = handle_none(row[7])
    to_return.fg_pct = handle_none(row[8])
    to_return.fg3m = handle_none(row[9])
    to_return.fg3a = handle_none(row[10])
    to_return.fg3_pct = handle_none(row[11])
    to_return.ftm = handle_none(row[12])
    to_return.fta = handle_none(row[13])
    to_return.ft_pct = handle_none(row[14])
    to_return.oreb = handle_none(row[15])
    to_return.dreb = handle_none(row[16])
    to_return.reb = handle_none(row[17])
    to_return.ast = handle_none(row[18])
    to_return.stl = handle_none(row[19])
    to_return.blk = handle_none(row[20])
    to_return.tov = handle_none(row[21])
    to_return.pf = handle_none(row[22])
    to_return.pts = handle_none(row[23])
    return to_return


def handle_undrafted(param):
    return int(param) if (param is not None and param != 'Undrafted') else None


def handle_jersey(param):
    if param is not None:
        try:
            return int(param.strip())
        except Exception:
            return None


def handle_empty_strings(param):
    return param if (param is not None and param.strip() != '') else None


if __name__ == '__main__':
    run()
