class Calculator():
   def __init__(self, value1, value2):
      self.value1 = value1
      self.value2 = value2
   
   def tambah(self):
      return self.value1 + self.value2
   def kurang(self):
      return self.value1 - self.value2
   def kali(self):
      return self.value1 * self.value2
   def bagi(self):
      return self.value1 / self.value2

val = input("Enter your value: ")

if "+" in val:
   value1, value2 = val.split("+")
   result = Calculator(int(value1), int(value2))
   print(result.tambah())
elif "-" in val:
   value1, value2 = val.split("-")
   result = Calculator(int(value1), int(value2))
   print(result.kurang())
elif "*" in val:
   value1, value2 = val.split("*")
   result = Calculator(int(value1), int(value2))
   print(result.kali())
elif "/" in val:
   value1, value2 = val.split("/")
   result = Calculator(int(value1), int(value2))
   print(result.bagi())