import codewars_test as test
from solution import count_patterns_from

@test.describe("Sample tests")
def sample():
    test.assert_equals(count_patterns_from('A',10), 0)
    test.assert_equals(count_patterns_from('A',0),  0)
    test.assert_equals(count_patterns_from('E',14), 0)
    test.assert_equals(count_patterns_from('B',1),  1)
    test.assert_equals(count_patterns_from('C',2),  5)
    test.assert_equals(count_patterns_from('E',2),  8)
    test.assert_equals(count_patterns_from('E',4),  256)