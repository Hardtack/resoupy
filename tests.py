import unittest
from resoup.tests import ResoupTest

loader = unittest.TestLoader()
test_cases = (ResoupTest,)
test_suite = unittest.TestSuite()
for tests in map(loader.loadTestsFromTestCase, test_cases):
    test_suite.addTests(tests)
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
