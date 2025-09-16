# Example file for working with classes
#

from xxlimited import new


class Person:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def get_info(self):
        return f"Person Name: {self.name}, Email: {self.email}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, email, age, college, grade):
        super().__init__(name, email, age)
        self.grade = grade
        self.college = college

    def get_info(self):
        return f"Student Name: {self.name}, Email: {self.email}, Age: {self.age}, College: {self.college}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, email, age, subject):
        super().__init__(name, email, age)
        self.subject = subject

    def get_info(self):
        return f"Teacher Name: {self.name}, Email: {self.email}, Age: {self.age}, Subject: {self.subject}"

p = Person("John Doe", "john.doe@example.com", 30)

s = Student("Jane Smith", "jane.smith@example.com", 20, "MIT", "A")

t = Teacher("Dr. Brown", "dr.brown@example.com", 45, "Physics")

print(p.get_info())
print(s.get_info())
print(t.get_info())
