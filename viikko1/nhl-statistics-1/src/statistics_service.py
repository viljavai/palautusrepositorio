from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self.reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def type_is_points(self, player):
        return player.points

    def type_is_goals(self, player):
        return player.goals

    def type_is_assists(self, player):
        return player.assists

    def top_type(self, type):
        if type == SortBy.POINTS:
            return self.type_is_points
        elif type == SortBy.GOALS:
            return self.type_is_goals
        elif type == SortBy.ASSISTS:
            return self.type_is_assists

    def top(self, how_many, type=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=self.top_type(type))
        result = []
        i = 0
        while i <= how_many-1:
            result.append(sorted_players[i])
            i += 1

        return result
