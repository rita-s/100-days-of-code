# # phrase = "Giraffe Academy"
# # print(phrase[0].lower())

# # print(type(int("100")))

# selfish = '1234567'
# # selfish[start:stop:stepover] strings are immutable = I cannot change the value unless I completely reassign the value

# sliced = selfish[0:5]
# print(sliced)


# # Logical Thinking:
# # Logical thinking refers to the ability to reason and solve problems in a systematic and organized manner. 
# # It involves analyzing information, identifying patterns, and making logical deductions. 
# # In programming, logical thinking is crucial for designing algorithms and solving complex problems. 
# # Here's an example of logical thinking in Python:

# # Checking if a number is even or odd
# def is_even_or_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

# is_even_or_odd(5)  # Output: 5 is odd
# is_even_or_odd(10) # Output: 10 is even
# # Algorithms:
# # An algorithm is a step-by-step procedure or set of instructions used to solve a specific problem or perform a particular task. 
# # It is a well-defined sequence of operations that can be implemented in any programming language. 
# # Algorithms provide a way to solve complex problems efficiently. 
# # Here's an example of an algorithm to find the maximum element in a list using Python:

# # Finding the maximum element in a list
# def find_max_element(lst):
#     if len(lst) == 0:
#         return None

#     max_element = lst[0]
#     for element in lst:
#         if element > max_element:
#             max_element = element

#     return max_element

# numbers = [4, 9, 2, 6, 1]
# max_num = find_max_element(numbers)
# print(f"The maximum number is: {max_num}")  # Output: The maximum number is: 9

# # Data Structures:
# # Data structures are containers or formats used to organize and store data efficiently. They provide different ways of representing and manipulating data, depending on the requirements of the problem. Examples of commonly used data structures include arrays, linked lists, stacks, queues, and dictionaries. Here's an example of using a dictionary data structure in Python:

# # Storing and accessing information using a dictionary
# student = {
#     "name": "John Smith",
#     "age": 20,
#     "major": "Computer Science",
#     "university": "XYZ University"
# }

# print(f"Student Name: {student['name']}")
# print(f"Age: {student['age']}")
# print(f"Major: {student['major']}")
# print(f"University: {student['university']}")

# # Object-Oriented Programming (OOP):
# # Object-Oriented Programming is a programming paradigm that focuses on representing concepts as objects, which are instances of classes. OOP promotes the use of objects to encapsulate data and behavior, making it easier to manage and manipulate complex systems. Python fully supports OOP concepts such as encapsulation, inheritance, and polymorphism. Here's an example of a simple class in Python:

# # Creating a class representing a car
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         return f"Car: {self.make} {self.model}, Year: {self.year}"

# # Creating an instance of the Car class
# my_car = Car("Toyota", "Camry", 2022)
# print(my_car.get_info())  # Output: Car: Toyota Camry, Year: 2022
# # In this example, the Car class encapsulates the make, model, and year of a car, 
# # and the get_info() method retrieves the information about the car.

#  # Built-in functions cover a wide range of functionalities and are commonly used in Python programming. 
#  # Here are explanations for some of the most common built-in functions in Python:

# print()
# # This function is used to display output on the console. It takes one or more arguments and prints them as text.
# print("Hello, World!")  # Output: Hello, World!

# len()
# # It returns the length or the number of items in an object such as a string, list, tuple, or dictionary.

# my_string = "Hello"
# length = len(my_string)
# print(length)  # Output: 5

# input()
# # This function allows the user to input data from the console. 
# # It displays a prompt message and waits for the user to enter input, which is returned as a string.

# name = input("Enter your name: ")
# print(f"Hello, {name}!")  # Output: Hello, [user's input]!

# type()
# # It returns the type of an object. It is useful for checking the type of a variable or value.

# number = 42
# print(type(number))  # Output: <class 'int'>
# int(), float(), str(), bool()
# # These functions are used for type conversion. They convert a value into an integer, float, string, or boolean, respectively.

# num_str = "42"
# num_int = int(num_str)
# print(num_int)  # Output: 42

# pi = 3.14
# pi_str = str(pi)
# print(pi_str)  # Output: '3.14'

# truth = bool(1)
# print(truth)  # Output: True

# range()
# # It generates a sequence of numbers. It takes one, two, or three arguments to specify the start, end, and step size of the sequence.

# for num in range(1, 6):
#     print(num)  # Output: 1 2 3 4 5
# sum()
# # This function returns the sum of all elements in an iterable, such as a list or tuple.

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)  # Output: 15
# max() and min()

# # These functions return the maximum and minimum value from an iterable, respectively.

# numbers = [1, 2, 3, 4, 5]
# max_num = max(numbers)
# min_num = min(numbers)
# print(max_num)  # Output: 5
# print(min_num)  # Output: 1

# # List slicing is a technique in Python that allows you to extract a portion or a subset of elements from a list. 
# # It provides a concise and efficient way to access specific elements or create new lists based on a range of indices. 
# # The general syntax for list slicing is list[start:end:step], where:
#     # start specifies the index at which the slice starts (inclusive).
#     # end specifies the index at which the slice ends (exclusive).
#     # step specifies the step or the increment between indices (optional).
#     # Examples to illustrate list slicing:

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Extracting a portion of the list
# subset = my_list[2:6]
# print(subset)  # Output: [2, 3, 4, 5]

# # Extracting elements from the beginning to a specific index
# subset = my_list[:5]
# print(subset)  # Output: [0, 1, 2, 3, 4]

# # Extracting elements from a specific index to the end
# subset = my_list[5:]
# print(subset)  # Output: [5, 6, 7, 8, 9]

# # Extracting elements with a step size
# subset = my_list[1:8:2]
# print(subset)  # Output: [1, 3, 5, 7]

# # Reversing a list using slicing
# reversed_list = my_list[::-1]
# print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# # In Python, lists are mutable data structures that allow for dynamic storage and manipulation of elements. They come with a variety of built-in methods that provide convenient ways to modify, access, and manipulate list data. Here are some commonly used list methods in Python:

# append(item)
# # Adds an element to the end of the list.

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]

# extend(iterable)
# # Appends multiple elements from an iterable to the end of the list.

# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# insert(index, item)
# # Inserts an element at a specific position in the list.

# my_list = [1, 2, 3]
# my_list.insert(1, 10)
# print(my_list)  # Output: [1, 10, 2, 3]

# remove(item)
# # Removes the first occurrence of the specified element from the list.

# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3, 2]

# pop(index=-1)
# # Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

# my_list = [1, 2, 3]
# removed_element = my_list.pop(1)
# print(removed_element)  # Output: 2
# print(my_list)  # Output: [1, 3]
# index(item)
# # Returns the index of the first occurrence of the specified element in the list.

# my_list = [1, 2, 3, 2]
# index = my_list.index(2)
# print(index)  # Output: 1
# count(item)
# # Returns the number of occurrences of the specified element in the list.

# my_list = [1, 2, 3, 2]
# count = my_list.count(2)
# print(count)  # Output: 2
# sort()
# # Sorts the elements of the list in ascending order.

# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3]
# reverse()
# # Reverses the order of the elements in the list.

# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]

# # In Python, you can represent a matrix or a multidimensional list using nested lists. 
# # A nested list is a list that contains other lists as its elements, allowing you 
# # to create a two-dimensional or multidimensional structure. 
# # Each inner list represents a row or a subarray within the matrix. 
# # Here's an example of creating and accessing elements in a matrix:

# # Creating a 2x3 matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# # Accessing individual elements
# print(matrix[0][0])  # Output: 1
# print(matrix[1][2])  # Output: 6

# # In this example, we have created a 2x3 matrix represented by a nested list. The first list [1, 2, 3] corresponds to the first row, and the second list [4, 5, 6] corresponds to the second row.
# # To access individual elements in the matrix, you use the square bracket notation with the row and column indices. In Python, indices start from 0, so matrix[0][0] accesses the element at the first row and first column, which is 1.
# # You can also perform various operations on matrices, such as matrix addition, multiplication, and transposition. Here's an example of matrix addition:

# # Matrix addition
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrix2 = [
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# result = []
# for i in range(len(matrix1)):
#     row = []
#     for j in range(len(matrix1[i])):
#         row.append(matrix1[i][j] + matrix2[i][j])
#     result.append(row)

# print(result)  # Output: [[8, 10, 12], [14, 16, 18]]

# # In this example, we have two matrices, matrix1 and matrix2. We iterate over the rows and columns of the matrices and add the corresponding elements to create a new matrix result containing the sum of the two matrices.
# # You can perform other matrix operations using similar concepts and nested loops.
# # Note that you can extend this concept to create multidimensional lists with more dimensions by adding additional nested lists. For example, a three-dimensional list would contain nested lists within nested lists.


# # Common List Patterns: Common patterns include appending, extending, and removing elements from a list, as well as iterating over a list using loops.

# # List Unpacking: Unpacking allows you to assign elements of a list to individual variables in a single line.

# # Dictionaries: Dictionaries are key-value pairs used to store and retrieve data using unique keys.

# # Dictionary Keys: Keys in a dictionary are unique identifiers associated with values.

# # Dictionary Methods: Dictionary methods include operations like getting, adding, updating, and removing items from a dictionary.

# # Tuples: Tuples are immutable sequences typically used to store related pieces of information.

# # Sets: Sets are unordered collections of unique elements used for membership testing and eliminating duplicates.

# # Truthy vs Falsey: Truthy values evaluate to True in a Boolean context, while falsey values evaluate to False.

# # "is" vs "==": "is" checks if two objects are the same object in memory, while "==" checks if two objects have the same value.

# # For Loops: For loops iterate over a sequence or iterable and execute a block of code for each item.

# # While Loops: While loops repeatedly execute a block of code as long as a condition is true.

# # Break, Continue, Pass: These statements modify the flow of loops; break exits the loop, continue skips the current iteration, and pass is a placeholder for future code.

# # Methods vs Functions: Methods are functions that belong to a specific object or class, while functions are standalone blocks of code.

# # Walrus Operator: The walrus operator (:=) allows assignment within an expression, enabling you to assign and use a value in a single line.

# # Scope and Scope Rules: Scope refers to the visibility and accessibility of variables, and follows a set of rules that define where variables can be accessed.

# # Global Keyword vs Nonlocal Keyword: The global keyword allows access to a global variable, while the nonlocal keyword is used to access a variable in the nearest enclosing scope outside of a function.

# # Enumerate Method: The enumerate() function adds a counter to an iterable, returning an iterator of tuples containing the index and the element.

# # Different Sorting Options: Python offers various sorting options, including sorting in ascending or descending order, sorting based on specific keys or attributes, and custom sorting using a key function.

# # Magical Methods (Dunder Methods): These special methods in Python classes provide functionality for operator overloading, object representation, and more.

# # Encapsulation: Encapsulation is the practice of bundling data and methods together within a class and controlling access to them using access modifiers.

# # Abstraction: Abstraction refers to representing complex data or behavior in a simplified and generalized manner.

# # Private vs Public Variables: Private variables are intended to be accessed only within the class, while public variables can be accessed from outside the class.

# # Inheritance: Inheritance allows a class to inherit attributes and methods from a parent class, promoting code reuse and creating a hierarchical structure.

# # Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common base class, enabling flexibility and interchangeable use.

# # super(): super() is a method used to call a parent class's methods and constructors from a child class.

# # Object Introspection: Object introspection refers to the ability to examine the type, attributes, and methods of an object at runtime.

# # Dunder Methods: Dunder methods are special methods that use double underscores (e.g., init) and provide specific functionality in classes.

# # Multiple Inheritance: Multiple inheritance is the ability to inherit from multiple parent classes, allowing a class to inherit attributes and methods from multiple sources.

# # Method Resolution Order: Method Resolution Order (MRO) determines the order in which methods are inherited and executed in the case of multiple inheritance.

# # Functional Programming: Functional programming is a programming paradigm that emphasizes the use of pure functions and avoids changing state or mutable data.

# # Pure Functions: Pure functions are functions that always produce the same output for the same input and have no side effects.

# # Map(), Filter(), Zip(), Reduce(): These are higher-order functions that operate on iterables and allow for concise and functional programming constructs.

# # Lambda Expressions: Lambda expressions are anonymous functions that can be defined in a single line without a formal function definition.

# # List Comprehensions: List comprehensions provide a concise way to create lists based on existing lists or iterables.

# # Decorators: Decorators are functions that modify the behavior of other functions or classes by wrapping them with additional functionality.

# # Higher Order Functions: Higher-order functions are functions that can take other functions as arguments or return functions as results.

# # Error Handling: Error handling is the practice of catching and managing exceptions or errors that may occur during program execution.

# # Generators: Generators are functions that allow the creation of iterators, enabling efficient memory usage for large sequences of values.

# # Modules: Modules are separate files that contain Python code, providing a way to organize and reuse code across multiple files.

# # Virtual Environments: Virtual environments are isolated Python environments that allow for separate package installations and dependencies for different projects.

# # File I/O: File I/O refers to reading from and writing to files on disk, allowing for persistent data storage and retrieval.

# # Regular Expressions: Regular expressions are patterns used to match and manipulate strings based on specific rules.

# # Testing: Testing involves writing test cases and executing them to verify the correctness and behavior of a program or code.


# # Appending elements to a list
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]

# # Extending a list with another list
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# # Removing an element from a list
# my_list = [1, 2, 3]
# my_list.remove(2)
# print(my_list)  # Output: [1, 3]

# # Unpacking a list
# numbers = [1, 2, 3]
# a, b, c = numbers
# print(a, b, c)  # Output: 1 2 3

# # Ignoring certain elements using the underscore (_)
# x, _, z = [4, 5, 6]
# print(x, z)  # Output: 4 6

# # Creating a dictionary
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A'}

# # Accessing values by keys
# print(student["name"])  # Output: John

# # Modifying a value
# student["age"] = 21
# print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

# # Accessing keys of a dictionary
# student = {"name": "John", "age": 20, "grade": "A"}
# keys = student.keys()
# print(keys)  # Output: dict_keys(['name', 'age', 'grade'])

# # Adding a new key-value pair
# student = {"name": "John", "age": 20}
# student["grade"] = "A"
# print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A'}

# # Removing a key-value pair
# del student["age"]
# print(student)  # Output: {'name': 'John', 'grade': 'A'}

# # Creating a tuple
# point = (3, 4)
# print(point)  # Output: (3, 4)

# # Accessing elements of a tuple
# x, y = point
# print(x, y)  # Output: 3 4

# # Creating a set
# fruits = {"apple", "banana", "orange"}
# print(fruits)  # Output: {'orange', 'apple', 'banana'}

# # Checking membership
# print("apple" in fruits)  # Output: True

# # Adding elements to a set
# fruits.add("grape")
# print(fruits)  # Output: {'grape', 'orange', 'apple', 'banana'}

# # Truthy values
# if 5:
#     print("Truthy")

# # Falsey values
# if 0:
#     print("Falsey")
# else:
#     print("Falsey")


# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # Output: True (a and b reference the same object)
# print(a is c)  # Output: False (a and c reference different objects)
# print(a == c)  # Output: True (a and c have the same values)

# # Iterating over a list
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

# # Output:
# # apple
# # banana
# # orange

# # Iterating over a range of numbers
# for num in range(1, 6):
#     print(num)

# # Output:
# # 1
# # 2
# # 3
# # 4
# # 5

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # Output:
# # 0
# # 1
# # 2
# # 3
# # 4

# # Break statement
# for num in range(1, 6):
#     if num == 3:
#         break
#     print(num)

# # Output:
# # 1
# # 2

# # Continue statement
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# # Output:
# # 1
# # 2
# # 4
# # 5

# # Pass statement
# for num in range(1, 6):
#     if num == 3:
#         pass
#     print(num)

# # Output:
# # 1
# # 2
# # 3
# # 4
# # 5

# # Function
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Output: Hello, Alice!

# # Method
# class Person:
#     def greet(self, name):
#         print(f"Hello, {name}!")

# person = Person()
# person.greet("Bob")  # Output: Hello, Bob!

# # Assigning a value based on a condition
# score = 80
# if (pass_score := score >= 60):
#     print("Passed")
# else:
#     print("Failed")

# # Output: Passed

# # Global scope
# global_var = 10

# def my_function():
#     # Local scope
#     local_var = 20
#     print(local_var)

# my_function()  # Output: 20
# print(global_var)  # Output: 10


# # Global variable
# count = 0

# def increment():
#     global count
#     count += 1
#     print(count)

# increment()  # Output: 1

# # Nonlocal variable
# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print(x)

#     inner()
#     print(x)

# outer()  # Output: nonlocal nonlocal

# fruits = ["apple", "banana", "orange"]

# # Enumerate with default start index (0)
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# # Output:
# # 0 apple
# # 1 banana
# # 2 orange

# # Enumerate with custom start index (1)
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# # Output:
# # 1 apple
# # 2 banana
# # 3 orange

# numbers = [4, 2, 7, 1, 5]

# # Sorting in ascending order
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # Output: [1, 2, 4, 5, 7]

# # Sorting in descending order
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print(sorted_numbers_desc)  # Output: [7, 5, 4, 2, 1]

# # Sorting based on custom key
# words = ["apple", "banana", "orange"]
# sorted_words = sorted(words, key=len)
# print(sorted_words)  # Output: ['apple', 'orange', 'banana']

# class MyList:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, index):
#         return self.data[index]

#     def __setitem__(self, index, value):
#         self.data[index] = value

# my_list = MyList([1, 2, 3, 4, 5])
# print(len(my_list))  # Output: 5
# print(my_list[2])  # Output: 3

# my_list[3] = 10
# print(my_list[3])  # Output: 10

# class Person:
#     def __init__(self, name):
#         self._name = name  # Protected attribute

#     def display_name(self):
#         print(self._name)

# person = Person("Alice")
# person.display_name()  # Output: Alice
# print(person._name)  # Output: Alice (can still access, but conventionally treated as protected)


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rectangle = Rectangle(5, 3)
# print(rectangle.area())  # Output: 15
# print(rectangle.perimeter())  # Output: 16

# class Person:
#     def __init__(self, name):
#         self._name = name  # Protected variable
#         self.__age = 25  # Private variable

# person = Person("Alice")
# print(person._name)  # Output: Alice
# # print(person.__age)  # Error: AttributeError: 'Person' object has no attribute '__age'
# print(person._Person__age)  # Output: 25 (accessing private variable using name mangling)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog("Buddy")
# print(dog.name)  # Output: Buddy
# print(dog.speak())  # Output: Woof!

# cat = Cat("Whiskers")
# print(cat.name)  # Output: Whiskers
# print(cat.speak())  # Output: Meow!

# def animal_speak(animal):
#     print(animal.speak())

# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# animal_speak(dog)  # Output: Woof!
# animal_speak(cat)  # Output: Meow!

# class Vehicle:
#     def __init__(self, name):
#         self.name = name

# class Car(Vehicle):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

# car = Car("BMW", "Blue")
# print(car.name)  # Output: BMW
# print(car.color)  # Output: Blue

# class Person:
#     def __init__(self, name):
#         self.name = name

# person = Person("Alice")

# print(type(person))  # Output: <class '__main__.Person'>
# print(dir(person))  # Output: list of attributes and methods of the person object

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# print(v3)  # Output: (6, 8)

# class A:
#     def method_a(self):
#         print("Method A")

# class B:
#     def method_b(self):
#         print("Method B")

# class C(A, B):
#     def method_c(self):
#         print("Method C")

# obj = C()
# obj.method_a()  # Output: Method A
# obj.method_b()  # Output: Method B
# obj.method_c()  # Output: Method C

# class A:
#     def common_method(self):
#         print("Method in A")

# class B(A):
#     def common_method(self):
#         print("Method in B")

# class C(A):
#     def common_method(self):
#         print("Method in C")

# class D(B, C):
#     pass

# obj = D()
# obj.common_method()  # Output: Method in B
# print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# # Pure Functions
# def multiply_by_two(n):
#     return n * 2

# result = multiply_by_two(5)
# print(result)  # Output: 10

# # Map()
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# # Filter()
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4]

# # Zip()
# fruits = ["apple", "banana", "orange"]
# quantities = [5, 3, 2]
# fruit_quantities = list(zip(fruits, quantities))
# print(fruit_quantities)  # Output: [('apple', 5), ('banana', 3), ('orange', 2)]

# # Reduce()
# from functools import reduce
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 120

# # Lambda expression as an anonymous function
# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)  # Output: 8

# numbers = [1, 2, 3, 4, 5]

# # Doubling each number in the list
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# # Selecting even numbers from the list
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)  # Output: [2, 4]

# def uppercase_decorator(func):
#     def wrapper(text):
#         result = func(text)
#         return result.upper()
#     return wrapper

# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # Output: HELLO, ALICE!

# def greeting():
#     return "Hello!"

# def greet(func):
#     print(func())

# greet(greeting)  # Output: Hello!

# try:
#     num = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")

# try:
#     file = open("nonexistent_file.txt", "r")
# except FileNotFoundError:
#     print("Error: File not found")

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib_gen = fibonacci_generator()
# for _ in range(10):
#     print(next(fib_gen))

# # Output: 0 1 1 2 3 5 8 13 21 34

# # Importing a module
# import math

# print(math.sqrt(25))  # Output: 5.0

# # Importing specific functions/classes from a module
# from datetime import datetime

# current_time = datetime.now()
# print(current_time)  # Output: Current date and time

# # Creating a virtual environment
# # $ python -m venv myenv

# # Activating the virtual environment
# # $ source myenv/bin/activate  (Linux/Mac)
# # $ myenv\Scripts\activate  (Windows)

# # Installing packages in the virtual environment
# # $ pip install package_name

# # Deactivating the virtual environment
# # $ deactivate

# # Writing to a file
# with open("my_file.txt", "w") as file:
#     file.write("Hello, World!")

# # Reading from a file
# with open("my_file.txt", "r") as file:
#     content = file.read()
#     print(content)  # Output: Hello, World!

# import re

# pattern = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
# text = "Contact us at info@example.com"

# matches = re.findall(pattern, text, re.IGNORECASE)
# print(matches)  # Output: ['info@example.com']

# import unittest

# def add_numbers(a, b):
#     return a + b

# class TestAddNumbers(unittest.TestCase):
#     def test_add_numbers(self):
#         result = add_numbers(2, 3)
#         self.assertEqual(result, 5)

# if __name__ == "__main__":
#     unittest.main()

# # Output:.
# # ----------------------------------------------------------------------
# # Ran 1 test in 0.001s

# # OK

# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @logging_decorator
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # Output: Calling greet
#                        #         Hello, Alice!

# def multiply(x):
#     return x * 2

# def add(x):
#     return x + 2

# def apply_operation(func, x):
#     return func(x)

# result1 = apply_operation(multiply, 3)
# result2 = apply_operation(add, 3)
# print(result1)  # Output: 6
# print(result2)  # Output: 5

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print("Error:", str(e))

# try:
#     file = open("nonexistent_file.txt", "r")
# except FileNotFoundError as e:
#     print("Error:", str(e))

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib_gen = fibonacci_generator()
# for _ in range(10):
#     print(next(fib_gen))

# # Output: 0 1 1 2 3 5 8 13 21 34

# # Importing a module
# import math

# print(math.sqrt(25))  # Output: 5.0

# # Importing specific functions/classes from a module
# from datetime import datetime

# current_time = datetime.now()
# print(current_time)  # Output: Current date and time

# # Creating a virtual environment
# # $ python -m venv myenv

# # Activating the virtual environment
# # $ source myenv/bin/activate  (Linux/Mac)
# # $ myenv\Scripts\activate  (Windows)

# # Installing packages in the virtual environment
# # $ pip install package_name

# # Deactivating the virtual environment
# # $ deactivate

# # Writing to a file
# with open("my_file.txt", "w") as file:
#     file.write("Hello, World!")

# # Reading from a file
# with open("my_file.txt", "r") as file:
#     content = file.read()
#     print(content)  # Output: Hello, World!

# import re

# pattern = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
# text = "Contact us at info@example.com"

# matches = re.findall(pattern, text, re.IGNORECASE)
# print(matches)  # Output: ['info@example.com']

# import unittest

# def add_numbers(a, b):
#     return a + b

# class TestAddNumbers(unittest.TestCase):
#     def test_add_numbers(self):
#         result = add_numbers(2, 3)
#         self.assertEqual(result, 5)

# if __name__ == "__main__":
#     unittest.main()


# item_list = ["one","two","three"]

# for item in item_list:
#     print(item)

# total = 0
# for number in range(1,101):
#     total += number
# print(total)    

# def greet(name, location):
#     print("Hello " + name + "!")
#     print("What's the weather like in " + location + "?")

# greet("Jane", "London")    

# dictionary = {
#     "Key": "Value",
#     "A": "Ala"
# }

# print(dictionary["Key"])
# total = []

# for i in range(1,6):
#     total.append(i)
# print(total)    

# my_dict = {"name": "John", "age": 25, "city": "New York"}

# for key in my_dict:
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)


# def my_function(a,b):
#     return a * b

# result = my_function(2,3)
# print(result)

#OOP

class Waiter: # creating a blueprint
    def __init__(self, name):
        self.name = name
        
waiter = Waiter("Betty")
print(waiter.name)
        
# betty = Waiter() # creating an object out of the blueprint
# betty.is_holding_plate = True
# betty.tables_responsible = [5,6]

# print(betty.tables_responsible)