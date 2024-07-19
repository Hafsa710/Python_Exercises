#Example 1: Adding Student in School database

class Student:

    #default constructors
    def __init__(self,fullname,marks):
         print("adding new student in database.")
         pass
    
    #parameterized constructors
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database.")

s1=Student("karan", 97)
print(s1.name, s1.marks)

s2=Student("arjun",67)
print(s2.name,s2.marks)