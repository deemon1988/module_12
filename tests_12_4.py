# Домашнее задание по теме "Логирование"

import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run1 = Runner('Mike', -5)
            logging.info(f'Sucessfuly created: name: {run1.name} speed: {run1.speed}')
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning(f" Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run1 = Runner(123)
            for i in range(10):
                run1.run()
            self.assertEqual(run1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning(' Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = Runner('Mike')
        run2 = Runner('Bob')
        for i in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance, 'Дистанции для run1 и run2 должны быть разными')


logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                    format="%(asctime)s | %(levelname)s | %(message)s")