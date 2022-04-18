
'''
variable scope has LEGB rule which is Local, Enclosing, Global, Built-in.
Jadi program akan membaca variable sesuai urutan ini
'''

x = "global x"
y = "global y"
def test():
   global y #membuat variable y menjadi glbal
   x = "local x"
   y = "local y"
   print(x)
   print(y)

def outer():
   z = "outer z"
   def inner():
      z = "inner z"
      print(z)
      
   inner()
   print(z)

test()
print(x)
print(y)
outer()