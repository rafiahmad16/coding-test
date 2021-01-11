import unittest
import ProductSum
import ast


class TestProductSum(unittest.TestCase):
    def test_ProductSum(self):
        with open("./test_case/dev.txt") as fp:
            test_cases = [line.rstrip('\n') for line in fp]
        #test_cases = open("./test_case/dev.txt").read().splitlines()
        for case in test_cases:
            i,o = case.split(" ")
            o = int(o)
            i = ast.literal_eval(i)
            result = ProductSum.ProductSum(i)
            self.assertEqual(result,o)
        

if __name__ == '__main__':
    unittest.main()