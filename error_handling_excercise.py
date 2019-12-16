while True:
  try:
    # get an integer for age
    age = int(input('What is your age? '))
    10/age
    print('You are',age,  'years old.')
  except ValueError as err:
    #if anything accept an int is enter print following error
    print(f'''
    please enter a number for your age.
    Error 10001
    {err}
    ''')
    #keep going
    continue
  except ArithmeticError as err:
    print(f'''
    Math Error
    Error 10002
    {err}
    ''')
    #exit out of the try
    break
  else:
    print('Thank you')
    break
  #runs always at the end of everything no matter what
  finally:
    print('Everything else completed')
print('Can you hear me?')
