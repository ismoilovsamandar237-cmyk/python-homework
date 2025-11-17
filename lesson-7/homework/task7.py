numbers = [1, 2, 3, 4]


squares = list(map(lambda x: x * x, numbers))
print(squares)  # [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]


evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]



def is_prime(n):
    if n < 2:
        return False


    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
print(is_prime(4))  # False
print(is_prime(7))  # True

def digit_sum(k):
    return sum(int(d) for d in str(k))

print(digit_sum(24))   # 6  (2 + 4)
print(digit_sum(502))  # 7  (5 + 0 + 2)

def print_powers_of_two(N):
    p = 1  # 2**0
    while p * 2 <= N:
        p *= 2
        print(p, end=" ")
        
print_powers_of_two(10)  # 2 4 8










