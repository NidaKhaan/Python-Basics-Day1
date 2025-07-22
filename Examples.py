""" This file contains examples of basic Python concepts including variables, control structures, functions, data types, lists, tuples, sets, dictionaries, comprehensions, and string formatting."""

# Example 1: Assigning different data types to variables
integer_var = 10       # integer type
float_var = 3.14       # float type
string_var = "Hello!"  # string type

print(integer_var, float_var, string_var)
# Example 2: Dynamic typing allows reassigning a variable to a new type
x = 5             # x is an integer
x = "now a text"  # x becomes a string
print(x)
# Example 3: Checking data types with the built-in type() function
a = True
b = 42
c = 2.718

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>


""" Control Structures (if, for, while) """

# Example 1: Using if, elif, else to check a number
num = 7
if num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")
else:
    print("Positive number")
# Example 2: For loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
# Example 3: While loop with a break condition
count = 0
while True:
    print("Count is", count)
    count += 1
    if count >= 3:
        break  # exit loop when count reaches 3


""" Functions """

# Example 1: Simple function with positional arguments
def greet(name, time_of_day):
    # name and time_of_day are positional args
    print(f"Good {time_of_day}, {name}!")

greet("Alice", "morning")
# Example 2: Function with default argument and *args
def summarize(title, *args):
    # *args captures extra positional arguments as a tuple
    print("Summary:", title)
    for point in args:
        print("-", point)

summarize("Shopping List", "Milk", "Bread", "Eggs")
# Example 3: Function using **kwargs for keyword arguments
def build_profile(first, last, **info):
    # **info captures extra named data as a dict
    profile = {"first_name": first, "last_name": last}
    profile.update(info)
    return profile

user = build_profile("John", "Doe", location="NYC", profession="Developer")
print(user)


""" Lists, Tuples, Sets, Dictionaries """

# Example 1: Lists and basic operations
colors = ["red", "green", "blue"]   # list literal
colors.append("yellow")             # add an element
print(colors[1])                    # access second element
# Example 2: Tuple unpacking and immutability
coordinates = (10.0, 20.0)  # tuple literal
x, y = coordinates          # unpacking into x and y
# coordinates[0] = 5.0     # would raise an error because tuples are immutable
print(x, y)
# Example 3: Sets for uniqueness and dictionaries for mappings
unique_numbers = {1, 2, 2, 3}  
print(unique_numbers)            # duplicates removed

person = {"name": "Jane", "age": 30}  
print(person["name"])            # retrieve value by key



""" List Comprehension and Set Comprehension """

# Example 1: List comprehension to square numbers
squares = [n * n for n in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
# Example 2: Filtering with list comprehension
evens = [n for n in range(10) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
# Example 3: Set comprehension to get unique first letters
words = ["apple", "banana", "apricot"]
first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'b'}



""" String Formatting (f-strings, .format) """

# Example 1: Using f-strings for inline evaluation
name = "Sam"
age = 25
print(f"{name} is {age} years old.")
# Example 2: Using the .format() method with positional placeholders
template = "{} scored {} out of {}"
print(template.format("Alice", 90, 100))
# Example 3: Named placeholders in .format()
report = "User {u} has {msg} unread messages"
print(report.format(u="bob", msg=5))
