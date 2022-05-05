import multiprocessing as mp
import time

start = time.perf_counter()


def do(seconds):
    print("111")
    time.sleep(seconds)
    print("222")


processes = []
for _ in range(10):
    p = mp.Process(target=do, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} seconds(s)")
