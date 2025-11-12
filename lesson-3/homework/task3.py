1
fruits = ["apple", "banana", "mango", "orange", "kiwi"]
print(fruits[2])

2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print(merged)

3
numbers = [10, 20, 30, 40, 50]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(new_list)

4
movies = ["Inception", "Avatar", "Interstellar", "Tenet", "Joker"]
movies_tuple = tuple(movies)
print(movies_tuple)

5
cities = ["Tashkent", "Paris", "London", "Tokyo"]
print("Paris" in cities)


6
nums = [1, 2, 3]
duplicated = nums * 2
print(duplicated)

7
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

8
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums[3:8])

9
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))

10
animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))

# 11
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)

# 12
lst = [1, 2, 3, 4]
tup = (10, 20, 30)
print(len(lst))
print(len(tup))

# 13
tup = (1, 2, 3, 4, 5)
lst = list(tup)
print(lst)

# 14
nums = (10, 50, 2, 45, 30)
print(max(nums))
print(min(nums))


# 15
words = ("data", "python", "analysis", "AI")
print(words[::-1])
