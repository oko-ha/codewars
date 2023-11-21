import codewars_test as test
from solution import dbl_linear

@test.describe("Twice linear")
def tests():
    test.assert_equals(dbl_linear(10), 22)
    test.assert_equals(dbl_linear(20), 57)
    test.assert_equals(dbl_linear(30), 91)
    test.assert_equals(dbl_linear(50), 175)