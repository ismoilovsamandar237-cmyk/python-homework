python -m venv myenv

myenv\Scripts\activate

deactivate


pip install requests numpy pandas

math_operations.py  
string_utils.py

# math_operations.py
# Basic math functions: add, subtract, multiply, divide

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b



# string_utils.py
# Basic string utilities

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
project/
│
├── math_operations.py
├── string_utils.py
│
├── geometry/
│     ├── __init__.py
│     └── circle.py
│
└── file_operations/
      ├── __init__.py
      ├── file_reader.py
      └── file_writer.py

# geometry/__init__.py
from .circle import calculate_area, calculate_circumference

# circle.py
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# file_operations/__init__.py
from .file_reader import read_file
from .file_writer import write_file

# file_reader.py

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

# file_writer.py

def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

# main.py

import math_operations
import string_utils
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

print(math_operations.add(5, 3))
print(string_utils.reverse_string("Samandar"))

print(calculate_area(10))
print(calculate_circumference(10))

write_file("test.txt", "Hello from Python!")
print(read_file("test.txt"))

package/
    __init__.py
    file1.py
    file2.py

