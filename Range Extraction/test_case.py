from solution import solution
import codewars_test as test

@test.describe("Range extraction")
def desc1():

    @test.it("Sample Tests")
    def it1():
        test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')