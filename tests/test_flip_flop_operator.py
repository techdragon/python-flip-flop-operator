from flip_flop_operator import flip_flop


def test_flip_flop_basic_functionality():
    for i in range(25):
        if (i == 4) | flip_flop | (i == 10):
            assert 5 <= i <= 9
        if (i == 12) | flip_flop | (i == 15):
            assert 13 <= i <= 14
