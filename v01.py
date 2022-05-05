import multiprocessing as mp
import time

start = time.perf_counter()

def do():
  print('111')
  time.sleep(1)
  print('222')

do()
do()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')