from cpu import CPU
from cache import CACHE
from controller import CONTROLLER
from bus import BUS
from mem import MEMORY

clock = 1

mainMem = MEMORY(clock)

dataBus = BUS(mainMem)

cahce1 = CACHE()
cahce2 = CACHE()
cahce3 = CACHE()
cahce4 = CACHE()


cont1 = CONTROLLER(cahce1, dataBus)
cont2 = CONTROLLER(cahce2, dataBus)
cont3 = CONTROLLER(cahce3, dataBus)
cont4 = CONTROLLER(cahce4, dataBus)


p1 = CPU(1, cont1, clock)
p2 = CPU(2, cont2, clock)
p3 = CPU(3, cont3, clock)
p4 = CPU(4, cont4, clock)

p1.compute()
p2.compute()
p3.compute()
p4.compute()

p2.manualCompute('P2: WRITE 1100 FFFF')
p2.manualCompute('P2: WRITE 1100 FFF2')  # write no func

print('#################################')
p1.controller.cache.printCache()
print('#################################')
p2.controller.cache.printCache()
print('#################################')
p3.controller.cache.printCache()
print('#################################')
p4.controller.cache.printCache()
print('#################################')


print(mainMem.data)

# P1: WRITE 1111 FFFF
