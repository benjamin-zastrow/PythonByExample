class Student:
    def __init__(self, name, age, gpa, is_on_probation): # constructor
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def setName(self, newName):
        self.name = newName
    def setAge(self, newAge):
        self.age = newAge
    def setGPA(self, newGPA):
        self.gpa = newGPA
    def setOnProbation(self, isOnProbation):
        self.is_on_probation = isOnProbation
    def isAdult(self):
        if self.age >= 18:
            return True
        else:
            return False

class UniversityStudent(Student): # inheritance from Student
    def __init_subclass__(self, uGrade):
        self.uGrade = uGrade
    def setUGrade(newuGrade):
        self.uGrade = newuGrade

ben = Student("Benjamin", 17, 1.1, False)
print(ben.is_on_probation)
print(ben.isAdult())