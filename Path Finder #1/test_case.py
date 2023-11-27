from solution import path_finder
import codewars_test as test

@test.it('Example 1')
def _():
    maze = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])
    test.assert_equals(path_finder(maze), True, repr(maze))

@test.it('Example 2')
def _():
    maze = "\n".join([
        ".W.",
        ".W.",
        "W.."
    ])
    test.assert_equals(path_finder(maze), False, repr(maze))

@test.it('Example 3')
def _():
    maze = "\n".join([
        "......",
        "......",
        "......",
        "......",
        "......",
        "......"
    ])
    test.assert_equals(path_finder(maze), True, repr(maze))

@test.it('Example 4')
def _():
    maze = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
    ])
    test.assert_equals(path_finder(maze), False, repr(maze))