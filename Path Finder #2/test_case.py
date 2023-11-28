from solution import path_finder
import codewars_test as test

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

test.assert_equals(path_finder(a), 4)
test.assert_equals(path_finder(b), False)
test.assert_equals(path_finder(c), 10)
test.assert_equals(path_finder(d), False)