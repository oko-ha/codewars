import codewars_test as test
from solution import Warrior

@test.it("Tom")
def _():
    tom = Warrior()
    test.assert_equals(tom.level, 1)
    test.assert_equals(tom.experience, 100)
    test.assert_equals(tom.rank, "Pushover")


@test.it("Bruce Lee")
def _():
    bruce_lee = Warrior()
    test.assert_equals(bruce_lee.level, 1)
    test.assert_equals(bruce_lee.experience, 100)
    test.assert_equals(bruce_lee.rank, "Pushover")
    test.assert_equals(bruce_lee.achievements, [])
    test.assert_equals(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
    test.assert_equals(bruce_lee.experience, 9100)
    test.assert_equals(bruce_lee.level, 91)
    test.assert_equals(bruce_lee.rank, "Master")
    test.assert_equals(bruce_lee.battle(90), "A good fight")
    test.assert_equals(bruce_lee.experience, 9105)
    test.assert_equals(bruce_lee.achievements, ["Defeated Chuck Norris"])