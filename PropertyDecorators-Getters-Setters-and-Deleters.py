class Employee:
   def __init__(self, first,last):
      self.first = first 
      self.last = last
   @property #membuat method menjadi seperti atribute
   def email(self):
      return f"{self.first}.{self.last}@email.com"
   @property
   def fullname(self):
      return f"{self.first} {self.last}"

   @fullname.setter #untuk bisa set ulang dengan memanggil method nya langsung
   def fullname(self,name):
      first, last = name.split(" ")
      self.first = first
      self.last = last

emp_1 = Employee("John", "Smith")
emp_1.first = "ali"

emp_1.fullname = "ali baba"

print(emp_1.email)
print(emp_1.fullname)