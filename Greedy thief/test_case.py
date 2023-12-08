from solution import greedy_thief
from preloaded import Item, check
import codewars_test as test

TESTS = [  #  [ [items, target, expected], ...]
      [
        [
          Item(weight=2, price=6),
          Item(weight=2, price=3),
          Item(weight=6, price=5),
          Item(weight=5, price=4),
          Item(weight=4, price=6),
        ],
        10,
        [
          Item(weight=2,price=6),
          Item(weight=2,price=3),
          Item(weight=4,price=6),
        ],
      ],
      [
        [
          Item(weight=9,price=1),
          Item(weight=9,price=2),
          Item(weight=9,price=3),
          Item(weight=9,price=4),
          Item(weight=9,price=5),
        ],
        10,
        [ Item(weight=9,price=5) ]
      ],
      [
        [
          Item(weight=1,price=1),
          Item(weight=2,price=2),
          Item(weight=3,price=3),
          Item(weight=4,price=4),
          Item(weight=5,price=5),
        ],
        10,
        [
          Item(weight= 2, price= 2 ),
          Item(weight= 3, price= 3 ),
          Item(weight= 5, price= 5 ),
        ]
      ],
      [
        [
          Item(weight=2,price=2),
          Item(weight=2,price=2),
          Item(weight=2,price=2),
          Item(weight=2,price=2),
          Item(weight=2,price=2),
          Item(weight=0,price=2),
          Item(weight=10,price=10),
          Item(weight=5,price=5),
        ],
        10,
        [ 
          Item(weight= 0, price= 2 ), 
          Item(weight= 10, price= 10 ),
        ]
      ],
      [
        # Weights ( prices too ) may be zero
        [Item(weight=0,price=1)],
        8,
        [Item(weight=0,price=1)]
      ],
      [
        # If no valid solution should return []
        [
          Item(weight=9,price=1),
          Item(weight=9,price=2),
          Item(weight=9,price=3),
          Item(weight=9,price=4),
          Item(weight=9,price=5),
        ],
        8,
        []
      ]
    ]

@test.it("Fixed case")
def _():
    for data in TESTS:
        check(*data, greedy_thief)

