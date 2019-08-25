#!/usr/bin/python3

import sys
import time
import _thread

# try:
#     strs = int(sys.argv[1])
# except IndexError:
#     print("EX: cpu_test 100000")
# else:
#     def fig_gen(max):
#         a, b, contador = 0, 1, 0
#         while contador < max:
#             a, b = b, a + b
#             yield a
#             contador += 1

#     inicio = time.time()
#     for n in fig_gen(strs):
#         print("{0} |".format(n))
#     fim = time.time() - inicio
#     if fim:
#         print("O processador levou {0} segundos".format(fim))

   

    
    

try:
    def fig_gen(max):
       a, b, contador = 0, 1, 0
       while contador < max:
           a, b = b, a + b
           yield a
           contador += 1
       inicio = time.time()
       for n in fig_gen(strs):
           print("{0} |".format(n))
       fim = time.time() - inicio
       if fim:
           print("O processador levou {0} segundos".format(fim))
    strs = int(sys.argv[1])
    _thread.start_new_thread( fig_gen, (strs) )
except IndexError:
    print("EX: cpu_test 100000")
except:
    print("Thread err")

            


