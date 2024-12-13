class Student:
    UniversityName = "NYU"
    def __init__(self , name , idnumber):
      self.name = name
      self.idnumber = idnumber
    def printinfo(self):
       print(self.name , self.idnumber , self.UniversityName)
    
student1 = Student("Melissa" , 43045)
student2 = Student("Rafe" ,43052 )
student1.printinfo()
student2.printinfo()
