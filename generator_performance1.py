#Generator 
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
# long_time is faster than long_time2 even though both do the samething. This processes faster by not holding things in memory and using resources more efficiently 
def long_time():
    print('1')
    for i in range(20000000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(20000000)):
        i*5


long_time()
long_time2()
