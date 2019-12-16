#Error Handling
def sum(num1, num2):
  try:
    return num1 + num2
  except TypeError as err:
  #except (TypeError, ZeroDivisionError) as err:
    #formated strings to call
    print(f'Please enter numbers {err}')

print (sum(1, 2))
