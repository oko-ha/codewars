import codewars_test as test
from solution import hamming

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hamming(1), 1, "hamming(1) should be 1")
        test.assert_equals(hamming(2), 2, "hamming(2) should be 2")
        test.assert_equals(hamming(3), 3, "hamming(3) should be 3")
        test.assert_equals(hamming(4), 4, "hamming(4) should be 4")
        test.assert_equals(hamming(5), 5, "hamming(5) should be 5")
        test.assert_equals(hamming(6), 6, "hamming(6) should be 6")
        test.assert_equals(hamming(7), 8, "hamming(7) should be 8")
        test.assert_equals(hamming(8), 9, "hamming(8) should be 9")
        test.assert_equals(hamming(9), 10, "hamming(9) should be 10")
        test.assert_equals(hamming(10), 12, "hamming(10) should be 12")
        test.assert_equals(hamming(11), 15, "hamming(11) should be 15")
        test.assert_equals(hamming(12), 16, "hamming(12) should be 16")
        test.assert_equals(hamming(13), 18, "hamming(13) should be 18")
        test.assert_equals(hamming(14), 20, "hamming(14) should be 20")
        test.assert_equals(hamming(15), 24, "hamming(15) should be 24")
        test.assert_equals(hamming(16), 25, "hamming(16) should be 25")
        test.assert_equals(hamming(17), 27, "hamming(17) should be 27")
        test.assert_equals(hamming(18), 30, "hamming(18) should be 30")
        test.assert_equals(hamming(19), 32, "hamming(19) should be 32")