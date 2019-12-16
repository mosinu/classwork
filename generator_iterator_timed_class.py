from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

class MyGen():
  current = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last

#  @performance
  def __iter__(self):
    return self

  @performance
  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current +=1
      return num
    raise StopIteration

gen = MyGen(0,100)
for i in gen:
  print(i)
#long_time()
