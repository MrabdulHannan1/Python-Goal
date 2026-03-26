#Lesson 1: Variables — names that hold values

# A variable is a label you choose. Python remembers the value for you.
name = "hanan"
age = 24
height_m = 1.75
loves_python = True

print("Hello,", name)
print("Age:", age, "| Height (m):", height_m, "| Loves Python:", loves_python)

# Types (what kind of value it is)
print(type(name))         # str — text
print(type(age))          # int — whole number
print(type(height_m))     # float — decimal number
print(type(loves_python))  # bool — True or False

# You can change a variable later (reassignment)
age = age + 1
print("Next year age:", age)

# f-strings: put values inside text easily
greeting = f"{name} is {age} years old."
print(greeting)

Print("come back ")