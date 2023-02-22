# Example of a class hierarchy that demonstrates inheritance, encapsulation, and methods

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        self._student_id = student_id

    def study(self):
        print(f"{self._name} is studying hard!")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = subject

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        self._subject = subject

    def teach(self):
        print(f"{self._name} is teaching {self._subject}!")

# Example usage of the classes and methods
person1 = Person("Alice", 30)
student1 = Student("Bob", 20, 1234)
teacher1 = Teacher("Charlie", 40, "Math")

print(person1.get_name())        # Output: "Alice"
print(student1.get_student_id()) # Output: 1234
print(teacher1.get_subject())    # Output: "Math"

student1.study()   # Output: "Bob is studying hard!"
teacher1.teach()   # Output: "Charlie is teaching Math!"

# Example of changing object attributes
person1.set_name("Dave")
print(person1.get_name())   # Output: "Dave"




#In this example, we define a Person class that has attributes for name and age, 
#as well as methods to get and set those attributes. We then define a Student 
#class and a Teacher class that inherit from the Person class and add additional 
#attributes and methods.#We also use encapsulation to make the name and age 
#attributes of Person private, by prefixing their names with an underscore. 
#This indicates that they should not be accessed directly from outside the class, 
#and instead should be accessed through the getter and setter methods.
#Finally, we create objects of each class and demonstrate how to use their 
#methods to perform actions, as well as how to change the values of their 
#attributes using the setter methods.




