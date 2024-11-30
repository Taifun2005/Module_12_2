import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = runner_and_tournament.Runner(name="Усэйн", speed=10)
        self.Andrey = runner_and_tournament.Runner(name="Андрей", speed=9)
        self.Nik = runner_and_tournament.Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():

            print(result)

    def test_race_usain_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_andrey_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_usain_andrey_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[len(results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
