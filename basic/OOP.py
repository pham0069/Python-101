# Python is OOP
# modularity: separation of code and behavior
# extensibility: objects can be extended to include new behaviors and attributes
# reusability: objects can be reused everywhere in application

# class - blueprint
# encapsulation: group variables and functions
class Person:
    # class variable, shared among all variables
    person_list = []
    __color = "GREEN" # how Python handle private, called name mangling
    #constructor
    # self refers to the instance  of Person class
    # we can access the instance related variables via self
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # refer to person_list needs to use self
        self.person_list.append(self.name)

    def show_name(self):
        print('My name is ' + self.name)
    def __str__(self):
        return '{%s, %s}' % (self.name, self.age)
    def __eq__(self, other):
        return other.name == self.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# object - intance
p1 = Person('Daniel', 25)
p2 = Person(age=20, name='Edward')
p1.show_name()
# this proves that person_list is shared btw p1 and p2
print(p1.person_list)
print(p2.person_list)

# not allowed as __ indicates "private variable"
# but it's not exactly "private variable" like Java
#print(p1.__color)

print(dir(p1)) # rename __color into _Person__color
print(p1._Person__color) # this refers to "private" variable color of Person

# print the object: use function __str__
print(p1)

# compare object: use function __eq__
p3 = Person('Daniel', 25)
print(p1 == p2)
print(p1 == p3)
print(p1 < p2)
