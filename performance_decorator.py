#decorator
from time import time

def performance(fn):
  def wrapper(*args, **kawrgs):
    #get current time
    t1 = time()
    result = fn(*args, **kawrgs)
    #get current time
    t2 = time()
    # subtract t1 from t2 in ms and compare
    print(f'took {t2 - t1} ms')
    return result
  return wrapper

@performance
def long_time():
  for i in range(2000000):
    i*5

long_time()
