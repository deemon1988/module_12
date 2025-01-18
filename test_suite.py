import unittest
import  test_calc
import test_new_calc
import test_runner
import test_tournament

calcTS = unittest.TestSuite()
#calcTS.addTest(unittest.makeSuite(test_calc.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalcTest))
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tournament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)

runner.run(runST)

