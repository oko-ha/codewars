import codewars_test as test
from solution import balanced_parens

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def ff():
        for n,exp in [ [0, [""]],
                       [1, ["()"]],
                       [2, ["(())","()()"]],
                       [3, ["((()))","(()())","(())()","()(())","()()()"]]]:
            actual = balanced_parens(n)
            actual.sort()
            test.assert_equals(actual, exp)