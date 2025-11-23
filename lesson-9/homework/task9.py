# 1
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # bu objectning ichki ma’lumotidir

    def area(self):
        return math.pi * (self.radius ** 2)  # πr²

    def perimeter(self):
        return 2 * math.pi * self.radius  # 2πr


circle1 = Circle(5)
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())

# 2
from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        return date.today().year - self.birth_year


p1 = Person("Samandar", "Uzbekistan", 2005)
print("Name:", p1.name)
print("Country:", p1.country)
print("Age:", p1.age())

# 3
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"


calc = Calculator()
print("Add:", calc.add(5, 3))
print("Divide:", calc.divide(10, 0))

# 4
import math

class Shape:
    def area(self):
        pass  # umumiy shaklda aniqlanmagan

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area())

# 5
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search(value, current.left)
        else:
            return self._search(value, current.right)


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(15))
print(bst.search(99))

# 6
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()

# 7
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

# 8
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())


cart = ShoppingCart()
cart.add_item("Apple", 2)
cart.add_item("Banana", 3)
print("Total:", cart.total_price())
cart.remove_item("Apple")
print("After removing Apple:", cart.items)

# 9
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "added")

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.display()
stack.pop()
stack.display()

# 10 
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()

# 11
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so‘m depozit qilindi.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so‘m yechildi.")
        else:
            print("Balans yetarli emas!")

    def display_balance(self):
        print(f"{self.name} balans: {self.balance} so‘m")


acc = BankAccount("Samandar", 1000)
acc.display_balance()
acc.deposit(500)
acc.withdraw(300)
acc.display_balance()





