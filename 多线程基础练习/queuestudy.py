import queue
from threading import Thread
import time
import random

num = 0

def product(tasks):
    global num
    while True:
        time.sleep(random.randint(1,3))
        num += 1
        tasks.put(num)
        print('product num {}'.format(num))



def consume(tasks):
    while True:
        time.sleep(random.randint(3,6))
        consume_num = tasks.get()
        print('consume num {}'.format(consume_num))


def main():
    tasks = queue.Queue()
    t1 = Thread(target=product,args=(tasks,))
    t2 = Thread(target=consume, args=(tasks,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__=='__main__':
    main()