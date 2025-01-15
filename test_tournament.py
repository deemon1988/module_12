# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
from pprint import pprint
from runner_and_tournament import Runner, Tournament



class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.run1 = Runner('Usein', 15)
        self.run2 = Runner('Max', 10)
        self.run3 = Runner('Nick', 5)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            finishers = {f'{k}: {str(v)}' for k, v in value.items()}
            print(finishers)

        # for elems in sorted(cls.all_results):
        #     finishers = {f'{k}: {str(v)}' for k, v in cls.all_results[elems].items()}
        #     print(finishers)


    def test_run1_run2(self):
        tournament1 = Tournament(90, self.run1, self.run3)
        self.__class__.all_results['1'] = tournament1.start()
        self.assertEqual(self.__class__.all_results['1'][2], 'Nick')

    def test_run2_run3(self):
        tournament2 = Tournament(90, self.run2, self.run3)
        self.__class__.all_results['2'] = tournament2.start()
        self.assertEqual(self.__class__.all_results['2'][2], 'Nick')

    def test_all_runners(self):
        tournament3 = Tournament(90, self.run1,self.run2, self.run3)
        self.__class__.all_results['3'] = tournament3.start()
        self.assertEqual(self.__class__.all_results['3'][3], 'Nick')


if __name__ == '__main__':
    unittest.main()