from solution import bowling_score
import codewars_test as test

@test.describe('Basic Tests')
def basic_tests():
    @test.it('maybe this bowler should put bumpers on')
    def maybe_this_bowler_should_put_bumpers_on():
        test.assert_equals(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
    @test.it('woah! Perfect game!')
    def perfect_game():
        test.assert_equals(bowling_score('X X X X X X X X X XXX'), 300)