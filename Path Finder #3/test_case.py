import codewars_test as test
from solution import path_finder

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = "\n".join([
          "000",
          "000",
          "000"
        ])

        b = "\n".join([
          "010",
          "010",
          "010"
        ])

        c = "\n".join([
          "010",
          "101",
          "010"
        ])

        d = "\n".join([
          "0707",
          "7070",
          "0707",
          "7070"
        ])

        e = "\n".join([
          "700000",
          "077770",
          "077770",
          "077770",
          "077770",
          "000007"
        ])

        f = "\n".join([
          "777000",
          "007000",
          "007000",
          "007000",
          "007000",
          "007777"
        ])

        g = "\n".join([
          "000000",
          "000000",
          "000000",
          "000010",
          "000109",
          "001010"
        ])

        test.assert_equals(path_finder(a), 0)
        test.assert_equals(path_finder(b), 2)
        test.assert_equals(path_finder(c), 4)
        test.assert_equals(path_finder(d), 42)
        test.assert_equals(path_finder(e), 14)
        test.assert_equals(path_finder(f), 0)
        test.assert_equals(path_finder(g), 4)