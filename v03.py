import multiprocessing as mp
import time

start = time.perf_counter()


def do():
    print("111")
    time.sleep(1)
    print("222")


processes = []
for _ in range(10):
    p = mp.Process(target=do)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} seconds(s)")
