#!/usr/bin/python3

import sys

try:
    strs = int(sys.argv[1])
except IndexError:
    print("EX: cpu_test 100000")
else:
    def fig_gen(max):
        a, b, contador = 0, 1, 0
        while contador < max:
            a, b = b, a + b
            yield a
            contador += 1


    for n in fig_gen(strs):
        print("{0} |".format(n))



