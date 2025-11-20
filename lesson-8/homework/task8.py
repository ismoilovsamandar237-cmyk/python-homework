# 1
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2
try:
    x = input("Enter integer: ")
    if not x.lstrip("-").isdigit():
        raise ValueError("Integer emas!")
    print(int(x))
except ValueError as e:
    print(e)

# 3
try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi.")

# 4
try:
    a = float(input())
    b = float(input())
    print(a+b)
except:
    raise TypeError("Ikkalasi ham son bo‘lishi kerak!")

# 5
try:
    with open("/root/secret.txt") as f:
        print(f.read())
except PermissionError:
    print("Ruxsat yo'q.")

# 6
lst = [1,2,3]

try:
    print(lst[5])
except IndexError:
    print("Bu indeks yo‘q!")

# 7
try:
    n = input("Enter: ")
except KeyboardInterrupt:
    print("Bekor qilindi (Ctrl+C)")

# 8
try:
    print(10/0)
except ArithmeticError:
    print("Matematik xato!")

# 9
try:
    with open("file.txt", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("UTF-8 emas kodlash.")

# 10
lst = [1,2,3]

try:
    lst.run()
except AttributeError:
    print("Bunday metod yo‘q!")

# Python File Input Output: Exercises, Practice, Solution
# 1
with open("file.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)

# 2
n = 3
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3
with open("file.txt", "a") as f:
    f.write("New line added!\n")

with open("file.txt", "r") as f:
    print(f.read())

# 4
from collections import deque

n = 3
with open("file.txt") as f:
    last_lines = deque(f, maxlen=n)

print("".join(last_lines))

# 5
lines = []
with open("file.txt") as f:
    for line in f:
        lines.append(line.strip())

print(lines)

# 6
with open("file.txt") as f:
    data = f.read()

# 7
arr = []
with open("file.txt") as f:
    for line in f:
        arr.append(line.strip())

# 8
with open("file.txt") as f:
    words = f.read().split()

longest = max(words, key=len)
print(longest)

# 9
with open("file.txt") as f:
    count = sum(1 for _ in f)

print(count)

# 10
from collections import Counter

with open("file.txt") as f:
    words = f.read().lower().split()

print(Counter(words))

# 11
import os
print(os.path.getsize("file.txt"), "bytes")

# 12
items = ["A", "B", "C"]

with open("output.txt", "w") as f:
    for item in items:
        f.write(item + "\n")

# 13
with open("src.txt") as s, open("dst.txt", "w") as d:
    for line in s:
        d.write(line)

# 14
with open("file1.txt") as f1, open("file2.txt") as f2, open("out.txt", "w") as out:
    for a, b in zip(f1, f2):
        out.write(a.strip() + " " + b)

# 15
import random

with open("file.txt") as f:
    print(random.choice(f.readlines()))

# 16 
f = open("file.txt")
print(f.closed)  # False
f.close()
print(f.closed)  # True


# 17
with open("file.txt") as f:
    data = f.read().replace("\n", "")

print(data)

# 18
import re

with open("file.txt") as f:
    words = re.findall(r"[A-Za-z0-9']+", f.read())

print(len(words))

# 19
chars = []

with open("file.txt") as f:
    for line in f:
        chars.extend(list(line))

print(chars)

# 20
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(letter)

# 21
import string

per_line = 5
letters = string.ascii_uppercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), per_line):
        f.write(" ".join(letters[i:i+per_line]) + "\n")











