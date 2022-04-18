class Dog: #parent class
   species = "Canis Familiaris" #atribute class
   def __init__(self, name, age): #method
      self.name = name
      self.age = age
   
   def __str__(self):
      return f"{self.name} is {self.age} years old"
   
   def speak(self, sound):
      return f"{self.name} is says {sound}"
   pass

class Bulldog(Dog): #child class
   def speak(self, sound = "woof"): #extend method
      return super().speak(sound) #memanggil isi method yang ada di parent class
   
   def sit(self):
      return f"{self.name} is sit right now"

buddy = Dog("Buddy", 3)
garox = Bulldog("Garox", 5)
print(buddy)
print(buddy.name)
print(buddy.speak("wanwan"))
print(garox.speak())
print(garox.sit())