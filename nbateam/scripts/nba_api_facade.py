import requests

BROWSER_HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


# Returns a list of all players in NBA history. Each row is an array, with data formatted into these columns:

# ["PERSON_ID","DISPLAY_LAST_COMMA_FIRST","DISPLAY_FIRST_LAST","ROSTERSTATUS",
#  "FROM_YEAR","TO_YEAR","PLAYERCODE","TEAM_ID","TEAM_CITY","TEAM_NAME","TEAM_ABBREVIATION",
#  "TEAM_CODE","GAMES_PLAYED_FLAG"]
def get_all_players():
    payload = {
        'LeagueID': '00',
        'IsOnlyCurrentSeason': '0',
        'Season': '2016-17'  # TODO update this to be dynamic
    }
    response = requests.get(
        'http://stats.nba.com/stats/commonallplayers',
        params=payload,
        headers=BROWSER_HEADERS
    )
    return response.json()['resultSets'][0]['rowSet']


# Returns an array of data about the player, formatted into these columns:

# ["PERSON_ID","FIRST_NAME","LAST_NAME","DISPLAY_FIRST_LAST","DISPLAY_LAST_COMMA_FIRST",
#  "DISPLAY_FI_LAST","BIRTHDATE","SCHOOL","COUNTRY","LAST_AFFILIATION","HEIGHT","WEIGHT",
#  "SEASON_EXP","JERSEY","POSITION","ROSTERSTATUS","TEAM_ID","TEAM_NAME","TEAM_ABBREVIATION",
#  "TEAM_CODE","TEAM_CITY","PLAYERCODE","FROM_YEAR","TO_YEAR","DLEAGUE_FLAG","GAMES_PLAYED_FLAG",
#  "DRAFT_YEAR","DRAFT_ROUND","DRAFT_NUMBER"]
def get_player_info(player_external_id):
    payload = {
        'LeagueID': '00',
        'IsOnlyCurrentSeason': '0',
        'PerMode': 'Totals',
        'PlayerID': player_external_id,
        'Season': '2016-17',
        'SeasonType': 'Regular+Season',
        'lineupIDs': '0',
        'lineupsPassed': 'false',
        'vsLineupIDs': '0'
    }
    response = requests.get(
        'http://stats.nba.com/stats/commonplayerinfo',
        params=payload,
        timeout=5,
        headers=BROWSER_HEADERS
    )
    return response.json()['resultSets'][0]['rowSet'][0]


# Returns a list of objects, each of which contain rows of season/career data about the player

# [0]['rowSet'] contains a list of a player's season total (regular season) stats
# [1]['rowSet'][0] contains a row of data of a player's career total (regular season) stats
# [2]['rowSet'] contains a list of a player's season total (postseason) stats
# [3]['rowSet'][0] contains a row of data of a player's career total (postseason) stats
def get_player_stats(player_external_id):
    payload = {
        'LeagueID': '00',
        'PerMode': 'Totals',
        'PlayerID': player_external_id
    }
    response = requests.get(
        'http://stats.nba.com/stats/playercareerstats',
        params=payload,
        headers=BROWSER_HEADERS
    )
    return response.json()['resultSets']
