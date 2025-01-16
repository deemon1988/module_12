# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.usein = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            finishers = {k: str(v) for k, v in value.items()}
            print(finishers)

    def test_run1_run2(self):
        tournament1 = Tournament(90, self.usein, self.nick)
        self.__class__.all_results['забег 1'] = tournament1.start()
        self.assertEqual(self.__class__.all_results['забег 1'][2], 'Ник')

    def test_run2_run3(self):
        tournament2 = Tournament(90, self.andrey, self.nick)
        self.__class__.all_results['забег 2'] = tournament2.start()
        self.assertEqual(self.__class__.all_results['забег 2'][2], 'Ник')

    def test_all_runners(self):
        tournament3 = Tournament(90, self.usein, self.andrey, self.nick)
        self.__class__.all_results['забег 3'] = tournament3.start()
        self.assertEqual(self.__class__.all_results['забег 3'][3], 'Ник')

    def test_place_distribution(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(results[1], self.usein)
        self.assertEqual(results[2], self.andrey)
        self.assertEqual(results[3], self.nick)


if __name__ == '__main__':
    unittest.main()
