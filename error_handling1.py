while True:
  try:
    # get an integer for age
    age = int(input('What is your age? '))
    print('You are',age,  'years old.')
  except ValueError:
    #if anything accept an int is enter print following error
    print('''
    please enter a number for your age.
    Error 10001
    ''')
  except ArithmeticError:
    print('''
    Math Error
    Error 10002
    ''')
  else:
    print('Thank you')
    break
