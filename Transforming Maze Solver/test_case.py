from preloaded import verify
import codewars_test as test
from solution import maze_solver

@test.describe('Example Tests')
def _():
    example_tests = (
        (
            (4,2,5,4),
            (4,15,11,1),
            ('B',9,6,8),
            (12,7,7,'X')
        ),
        (
            (6,3,10,4,11),
            (8,10,4,8,5),
            ('B',14,11,3,'X'),
            (15,3,4,14,15),
            (14,7,15,5,5)
        ),
        (
            (9,1,9,0,13,0),
            (14,1,11,2,11,4),
            ('B',2,11,0,0,15),
            (4,3,9,6,3,'X')
        ),
        (
            ('B',6,12,15,11),
            (8,7,15,7,10),
            (13,7,13,15,'X'),
            (11,10,8,1,3),
            (12,6,9,14,7)
        ),
        (
            (6,3,0,9,14,13,14),
            ('B',14,9,11,15,14,15),
            (2,15,0,12,6,15,'X'),
            (4,10,7,6,15,5,3),
            (7,3,13,13,14,7,0)
        ),
    )
    example_sols = (
        ['NNE', 'EE', 'S', 'SS'],
        ['', '', 'E', '', 'E', 'NESE'],
        ['E', 'SE', '', 'E', 'E', 'E'],
        None,
        None
    )

    for i,v in enumerate(example_tests):
        @test.it(f'Example test {i+1}')
        def _():
            test.expect(*verify(v,maze_solver(v),example_sols[i]))
