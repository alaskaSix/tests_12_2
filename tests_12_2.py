import runner_and_tournament as rn
import unittest




class Tournament(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = rn.Runner('Усэйн', 10)
        self.andrey = rn.Runner('Андрей', 9)
        self.nick = rn.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_tournament_1(self):
        test1 = rn.Tournament(90, self.usain, self.nick)
        test1_result = {k: str(v) for k, v in test1.start().items()}
        Tournament.all_results.append(test1_result)
        self.assertTrue(test1_result[2], 'Ник')

    def test_tournament_2(self):
        test2 = rn.Tournament(90, self.andrey, self.nick)
        test2_result = {k: str(v) for k, v in test2.start().items()}
        Tournament.all_results.append(test2_result)
        self.assertTrue(test2_result[2], 'Ник')

    def test_tournament_3(self):
        test3 = rn.Tournament(90, self.usain, self.nick, self.nick)
        test3_result = {k: str(v) for k, v in test3.start().items()}
        Tournament.all_results.append(test3_result)
        self.assertTrue(test3_result[3], 'Ник')

    if __name__ == "__main__":
        unittest.main()