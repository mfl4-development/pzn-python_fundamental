# make variables like labeling a box
name = "Han"  # box named 'name' contains text 'Han'
age = 22  # box named 'age' contains number 22
height = 169.5  # box named 'height' contains number 169.5

first_name = "Far"

print(type(name))  # output: <class 'str'>
print(type(age))  # output: <class 'int'>
print(type(height))  # output: <class 'float'>

poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(type(poem))  # output: <class 'str'>

is_happy = True
is_raining = False
print(type(is_happy))  # output: <class 'bool'>

# basic assignments
name = "A-na"
age = 17
height = 169.2
is_active = True

# multiple assignments
x = y = z = 0  # all variables x, y, z are assigned to 0
a, b, c = 1, 2, 3  # a=1, b=2, c=3
name, age = "Ian", 16  # name="Ian", age=16

# changing variable values
score = 50
print(score)  # output: 50
score = 75  # score variable is updated to 75
print(score)  # output: 75

length = 10
width = 5
area = length * width  # area is calculated using length and width

print("Area : ", area)  # output: Area : 50
