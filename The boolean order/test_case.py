from solution import solve
import codewars_test as test

@test.it("Basic tests")
def basic_tests():
    test.assert_equals(solve("tft","^&"),2)
    test.assert_equals(solve("ttftff","|&^&&"),16)
    test.assert_equals(solve("ttftfftf","|&^&&||"),339)
    test.assert_equals(solve("ttftfftft","|&^&&||^"),851)
    test.assert_equals(solve("ttftfftftf","|&^&&||^&"),2434)
