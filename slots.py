import random


class slots:
    """Defines the reels of the slot machine"""

    def __init__(self):
        # The reels
        self.reels = [
            [
                2,
                7,
                1,
                3,
                6,
                4,
                1,
                3,
                5,
                4
            ],
            [
                2,
                3,
                1,
                3,
                7,
                4,
                5,
                6,
                1,
                7
            ],
            [
                5,
                2,
                4,
                3,
                3,
                7,
                6,
                2,
                1,
                4
            ],
        ]
        self.weights = [
            [
                112,
                9,
                144,
                20,
                50,
                17,
                150,
                120,
                412,
                37
            ],
            [
                139,
                72,
                122,
                34,
                9,
                9,
                412,
                50,
                317,
                9
            ],
            [
                288,
                91,
                23,
                88,
                28,
                9,
                55,
                57,
                164,
                47
            ],
        ]

        self.paytable = {1 : 18, 2 : 23, 3 : 23, 4 : 46, 5 : 11, 6 : 4, 7 : 48}
        self.starting_amount = 100
        self.max_bet = 10
        self.min_bet = .25
        self.bet_inc = .25
