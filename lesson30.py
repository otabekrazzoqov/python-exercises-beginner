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

#*****************************************************************************

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Person):
            return Person(f"{self.name} and {other.name}", self.age + other.age)
        return NotImplemented

# create objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Charlie", 20)

# use dunder methods
print(p1)               # prints "Alice (25)"
print(repr(p2))         # prints "Person('Bob', 30)"
print(p1 == p2)         # prints False
print(p1 == Person("Alice", 25))   # prints True
print(p1 < p2)          # prints True
print(p2 < p3)          # prints False
print(p1 + p2)          # prints "Alice and Bob (55)"




#*****************************************************************************



import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

# Create a list of Person objects
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 40)]

# Serialize the list to a file using pickle.dump()
with open("people.pickle", "wb") as f:
    pickle.dump(people, f)

# Deserialize the list from the file using pickle.load()
with open("people.pickle", "rb") as f:
    loaded_people = pickle.load(f)

# Print the deserialized list
for person in loaded_people:
    print(person)










