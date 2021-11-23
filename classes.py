class Person():
   age = 0
   height = 0
   name = ''
   lastname = ''

   # Constructor
   def __init__(self, init_name = "Galymzhan", \
                      init_lastname = "Kazhymurat", \
                      init_age = 19, \
                      init_height = 165):
     self.name = init_name
     self.lastname = init_lastname
     self.age = init_age
     self.height = init_height
  
class Student(Person):
  # 1 nemese 2 attribut kosu kerek
   math_score =  0
   history_score =  0
   programming_score =  0
   def __init__(self,init_name,init_lastname,init_age,init_height,init_mathscore,init_historyscore,init_progscore):
        super().__init__(init_name, init_lastname, init_age, init_height)
        self.math_score = init_mathscore 
        self.history_score = init_historyscore
        self.programming_score=init_progscore
  
   def print_info(self):
      print("Name:", self.name, self.lastname)
      print("Age:", self.age)
      print("Height:", self.height)
      print("Mathematics score:",self.math_score)
      print("History score:",self.history_score)
      print("Programming score:",self.programming_score)


# Teacher class
class Teacher(Person):
  # 1 nemese 2 attribut kosu kerek
  subject=''
  # jana attributtrga getter/setter metodtar jasau
  # init, print_info - ozgeris jasau kerek
  # init-ta Person-nin jane Studenttin manderin berip
  # super() arkyly  Person-nin manderin initsializatsiya jasau
  # def print_info():
  #    ..... + jana attributtardy da shygaru kerek
  def __init__(self,init_name,init_lastname,init_age,init_height,init_subject):
        super().__init__(init_name, init_lastname, init_age, init_height)
        self.subject = init_subject

  def print_info(self):
       print("Name:", self.name, self.lastname)
       print("Age:", self.age)
       print("Height:", self.height)
       print("Subject:",self.subject)


 
if __name__ == "__main__":
   stud1=Student("No","Mercy",19,165,100,95,100)
   stud1.print_info()
   teacher=Teacher("Teach","Me",107, 50, "Mathematics")
   teacher.print_info()
