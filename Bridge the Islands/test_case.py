from solution import bridge
import codewars_test as test

@test.it("Sample tests")
def sample_tests():
    test.assert_equals(bridge([(0, 0), (1, 0), (1, 1)]), 2)
    test.assert_approx_equals(bridge([(0, 0), (5, 5)]), 7.071067812)
    test.assert_approx_equals(bridge([(0, 0), (5, 5), (3, 3)]), 7.071067812)
    test.assert_approx_equals(bridge([(0, 0), (5, 5), (3, 3), (2, 4)]), 8.485281374)
    test.assert_approx_equals(bridge([(0, 0), (0, 4), (1, 3), (1, 5), (4, 0), (5, 1)]), 11.404918347)
    test.assert_approx_equals(bridge([(0, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4)]), 12)