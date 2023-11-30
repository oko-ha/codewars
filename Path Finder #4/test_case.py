import codewars_test as test
from solution import i_am_here

def where_are_you(path, result):
     test.assert_equals(i_am_here(path), result, path)

where_are_you('',       [0, 0])
where_are_you('RLrl',   [0, 0])
where_are_you('r5L2l4', [4, 3])