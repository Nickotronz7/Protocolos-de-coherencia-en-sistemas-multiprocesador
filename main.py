from cpu import CPU
from mem import MEMORY
from cache import CACHE
from control import CONTROL
from bus import BUS
import random


def main():
    clock = 1
    mainMem = MEMORY(clock)
    dataBus = BUS(mainMem)

    c1 = CPU(1, CACHE(), CONTROL(), clock, dataBus)
    c2 = CPU(2, CACHE(), CONTROL(), clock, dataBus)
    c3 = CPU(3, CACHE(), CONTROL(), clock, dataBus)
    c4 = CPU(4, CACHE(), CONTROL(), clock, dataBus)
    
    for i in range(10):
        c1.compute()
        c2.compute()
        c3.compute()
        c4.compute()

    mainMem.viewData()

if __name__ == '__main__':
    main()
