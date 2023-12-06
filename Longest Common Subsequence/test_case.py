import codewars_test as test
from solution import lcs


@test.describe("Tests")
def test_group():
    @test.it("Fixed tests")
    def test_case():
        test.assert_equals(lcs("", ""), "")
        test.assert_equals(lcs("abc", ""), "")
        test.assert_equals(lcs("", "abc"), "")
        test.assert_equals(lcs("a", "b"), "")
        test.assert_equals(lcs("a", "a"), "a")
        test.assert_equals(lcs("abc", "a"), "a")
        test.assert_equals(lcs("abc", "ac"), "ac")
        test.assert_equals(lcs("abcdef", "abc"), "abc")
        test.assert_equals(lcs("abcdef", "acf"), "acf")
        test.assert_equals(lcs("anothertest", "notatest"), "nottest")
        test.assert_equals(lcs("132535365", "123456789"), "12356")
        test.assert_equals(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final")
        test.assert_equals(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq")
