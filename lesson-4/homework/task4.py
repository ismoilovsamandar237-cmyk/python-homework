# 1
data = {'a': 3, 'b': 1, 'c': 2}

# 🔼 Ascending order
asc = dict(sorted(data.items(), key=lambda x: x[1]))

# 🔽 Descending order
desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)

# 2
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {}
for d in (dic1, dic2, dic3):
    merged.update(d)

print(merged)

# 4
n = 5
squares = {x: x**2 for x in range(1, n+1)}
print(squares)

# 5
squares_15 = {x: x**2 for x in range(1, 16)}
print(squares_15)

# 6
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 7
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# 8
nums = {1, 2, 3}
nums.add(4)
nums.update([5, 6, 7])  # bir nechta element qo‘shish
print(nums)

# 9
nums = {1, 2, 3, 4, 5}
nums.remove(3)
nums.discard(8)  # 8 yo‘q, ammo xato bermaydi
print(nums)

# 10
nums = {1, 2, 3, 4, 5}
if 3 in nums:
    nums.remove(3)
print(nums)














