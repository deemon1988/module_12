# Домашнее задание по теме "Систематизация и пропуск тестов"

import unittest
import test_runner
import test_tournament

run_tourST = unittest.TestSuite()
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tourST)