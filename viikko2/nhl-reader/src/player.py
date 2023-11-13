import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
    
    def total_points(self):
        return self.assists + self.goals

    def __str__(self):
        return  f"{self.name}, {self.nationality}, {self.assists}, {self.goals}, {self.penalties}, {self.team}, {self.games}"

class PlayerReader:
    def __init__(self, url):
        self._url = url
    
    def get_players(self):
        response = requests.get(self._url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        fin_players = []
        for player in self.players:
            if player.nationality == nationality:
                fin_players.append(player)
        
        result = []
        fin_players.sort(key=lambda player: player.total_points(), reverse=True)
        for player in fin_players:
            result.append(f"{player.name}    {player.team}   {player.goals} + {player.assists} = {player.total_points()}")

        return result