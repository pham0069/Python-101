# string is a sequence of character
# can use either double quote or single quote
# strings are one-dimensional array, with first index = 0
# there are no chars in Python - characters ar strings with single char
name = 'Albert Camus'
print(type(name))
print(name[0]) # first char
print(name[-1]) # last char
print(name[1:5]) # substring
age_string = "34"
print(name + age_string) # concatenate
age = 34
# print(name + age) # invalid - cannot concatenate string and number
print('Use format to print number value {}'.format(age))

s = '0123456789'

# array indexes - random index
print(s[0]) #0

# string slicing with : operator
# range including the start and excluding the end
print(s[2:7]) #23456

# not specify index -> whole string
print(s[:]) #0123456789

# we can define the step size
# positive value: left to right
print(s[1:8:3]) #147
# negative value: right to left
print(s[8:1:-2]) #8642
