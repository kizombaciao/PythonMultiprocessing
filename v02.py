import multiprocessing as mp
import time

start = time.perf_counter()

def do():
  print('111')
  time.sleep(1)
  print('222')

p1 = mp.Process(target=do)
p2 = mp.Process(target=do)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')