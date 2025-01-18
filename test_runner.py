# Домашнее задание по теме "Простые Юнит-Тесты"
import unittest
import runner
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run1 = Runner('Mike')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run1 = Runner('Mike')
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = Runner('Mike')
        run2 = Runner('Bob')
        for i in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance, 'Дистанции для run1 и run2 должны быть разными')


if __name__ == '__main__':
    unittest.main()
