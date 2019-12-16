def my_decorator(func):
  def wrap_func():
    func()
  return wrap_func

@my_decorator
def hello():
  #print('hello baby duck')
    print('''
    Hello Baby Duck!
       ..---..
     .'  _    `.
 __..'  (o)    :
`..__          ;
     `.       /
       ;      `..---...___
     .'                   `~-. .-')
    .                         ' _.'
   :                           :
   \                           '
    +                         J
     `._                   _.'
        `~--....___...---~' mh
        ''')
hello()
