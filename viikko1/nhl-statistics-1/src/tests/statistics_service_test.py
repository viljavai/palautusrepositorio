import unittest
from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
    
    def test_search_no_name(self):
        player = self.stats.search("Testi")
        self.assertEqual(player, None)
    
    def test_team(self):
        players = self.stats.team("EDM")
        result = []
        for player in players:
            result.append(player.name)
        self.assertEqual(result, ["Semenko", "Kurri", "Gretzky"])

    def test_top_no_parameter(self):
        players = self.stats.top(2)
        result = []
        for player in players:
            result.append(player.name)
        self.assertEqual(result, ["Gretzky", "Lemieux"])

    def test_top_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        result = []
        for player in players:
            result.append(player.name)
        self.assertEqual(result, ["Lemieux", "Yzerman"])
    
    def test_top_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        result = []
        for player in players:
            result.append(player.name)
        self.assertEqual(result, ["Gretzky", "Yzerman"])
    
    def test_top_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        result = []
        for player in players:
            result.append(player.name)
        self.assertEqual(result, ["Gretzky", "Lemieux"])
    