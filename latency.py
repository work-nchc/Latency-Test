from time import sleep, time
from random import uniform
from numpy import zeros

cycle = 5
precision = 0.001
msg_target = '================='
mdg_instruction = (
    'Press ENTER when seeing {}. (cycle: {})\nPress ENTER to start:'.format(
        msg_target, cycle))
msg_result = 'latency: {}({}) ms'
sleep_short = 1
sleep_long = 2

t0 = zeros(cycle)
t1 = zeros(cycle)
input(mdg_instruction)
for i in range(cycle):
    sleep(uniform(sleep_short, sleep_long))
    print(msg_target)
    t0[i] = time()
    input()
    t1[i] = time()
lat = t1 - t0
print(msg_result.format(
    int(lat.mean() // precision), int(lat.std() // precision)))
