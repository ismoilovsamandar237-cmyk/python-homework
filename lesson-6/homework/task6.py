def add_underscores(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0
    i = 0
    
    while i < len(txt):
        ch = txt[i]
        result += ch
        count += 1
        
        if count == 3:
            if i != len(txt) - 1:
                if ch in vowels:
                    result += txt[i + 1]
                    i += 1
                result += "_"
            count = 0
        
        i += 1
    
    if result.endswith("_"):
        result = result[:-1]
        
    return result

n = int(input())

for i in range(n):
    print(i * i)

i = 1
while i <= 10:
    print(i)
    i += 1

# 2
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 3
n = int(input("Enter number: "))
total = 0

for i in range(1, n+1):
    total += i

print("Sum is:", total)

# 4
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)

# 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

# 6
num = int(input("Enter number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Digits count:", count)

# 7 
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# 8

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# 9
for i in range(-10, 0):
    print(i)

# 10 

for i in range(5):
    print(i)
print("Done!")

# 11

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 12
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# 13
n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print(f"{n}! = {fact}")

from collections import Counter

def uncommon(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for key in (set(c1) | set(c2)):
        diff = abs(c1[key] - c2[key])
        result.extend([key] * diff)

    return result


