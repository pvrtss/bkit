from contextlib import contextmanager
import time

class cm_timer_1():
    def __init__(self):
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time: {}'.format(time.time() - self.start_time))

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    print('time: {}'.format(time.time() - start_time))

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1)
        time.sleep(1)

    with cm_timer_2():
        time.sleep(1)