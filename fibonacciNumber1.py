# Here is an example generator which calculates fibonacci numbers:
# generator version
def fib(number):
    a =  0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(100):
    print(x)

def isPrime(number) : 
  
    # Corner cases 
    if (number <= 1) : 
        return False
    if (number <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

#list
def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

#print(fib2(100))
