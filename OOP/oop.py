# Goal of this program is to explore Object Orientated Programming in Python

#Objects allow us to store data and reuse methods 
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def getName(self):
#         return self.name

# d = Dog("Tim")
# print(d.getName())
# #print(type(d))

#**********************************************************************************#

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade #a grade from 0-100

#     def get_grade(self):
#         return self.grade
    
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value/ len(self.students)


# s1 = Student("Tim",19,95)
# s2 = Student("Bill",19,75)
# s3 = Student("Jill",18,60)

# course = Course("Science",2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())

#**********************************************************************************#
#Exploring the idea of inheritance 
# class Pet:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old.")
#     def speak(self):
#         print("Who am I?")

# class Cat(Pet):
#     def __init__(self,name,age,color):
#         super().__init__(name,age)
#         self.color = color
#     def speak(self):
#         print("meow")
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
    
# class Dog(Pet):
#     def speak(self):
#         print("meow")

# p = Cat("Tim", 19, "Brown")
# p.show()

#**********************************************************************************#
#Explore class attributes
# class Person:
#     number_of_people = 0 # Considered ATTRIBUTES

#     def __init__(self,name):
#         self.name = name
#         Person.add_person()

#     @classmethod
#     def number_of_people_(cls):#only access the class attributes and nothing else
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#          cls.number_of_people +=1

# p1 = Person("tim")
# p2 = Person("Jill")
# Person.number_of_people = 8
# print(p2.number_of_people)# attribute not specific to a method is accessible
#print(Person.number_of_people())

#**********************************************************************************#
#Intro to static methods
# class Math:

#     @staticmethod#dont need access to anything 
#     def add5(x):
#         return x+5

# print(Math.add5(5))#static methods allow for direct calcs