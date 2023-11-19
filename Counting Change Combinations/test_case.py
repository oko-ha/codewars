from solution import count_change
import codewars_test as test

@test.describe('Counting change combinations')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(count_change(4, [1,2]), 3)
        test.assert_equals(count_change(10, [5,2,3]), 4)
        test.assert_equals(count_change(11, [5,7]), 0)
        test.assert_equals(count_change(0, [1,2]), 1)