def generator_function(num):
  for i in range(num):
    #pause function
    yield i

for item in generator_function(100):
  print(item)

