from bases import Bases
bases = Bases()


def convertor(base: int, number: int):
    return bases.toBase(number, base)
