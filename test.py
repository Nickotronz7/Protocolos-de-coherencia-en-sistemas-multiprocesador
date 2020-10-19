from cpu import CPU
from cache import CACHE
from controller import CONTROLLER
from bus import BUS
from mem import MEMORY

clock = 1

mainMem = MEMORY(clock)
dataBus = BUS(mainMem)

p1 = CPU(1, CONTROLLER(CACHE(), dataBus), clock)
p2 = CPU(2, CONTROLLER(CACHE(), dataBus), clock)
p3 = CPU(3, CONTROLLER(CACHE(), dataBus), clock)
p4 = CPU(4, CONTROLLER(CACHE(), dataBus), clock)

p1.compute()
p2.compute()
p3.compute()
p4.compute()

