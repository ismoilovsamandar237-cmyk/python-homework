#1
# todo_app.py
# Simple CLI ToDo list application
# Run: python todo_app.py

from datetime import datetime

class Task:
    def __init__(self, title, description='', due_date=None, status='pending'):
        """
        Task class:
        - title: short title string
        - description: longer description string
        - due_date: string in YYYY-MM-DD or None
        - status: 'pending' or 'done'
        """
        self.title = title
        self.description = description
        # store due_date as date object or None
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d').date() if due_date else None
        self.status = status

    def mark_done(self):
        self.status = 'done'

    def is_incomplete(self):
        return self.status != 'done'

    def __str__(self):
        due = self.due_date.isoformat() if self.due_date else 'No due'
        return f"[{self.status.upper():6}] {self.title} (Due: {due}) - {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_task_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            return True
        return False

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [t for t in self.tasks if t.is_incomplete()]


def main():
    todo = ToDoList()

    # sample tasks for quick testing
    todo.add_task(Task('Buy milk', '2 liters', '2025-12-01'))
    todo.add_task(Task('Finish SQL homework', 'Lesson 18 tasks', '2025-11-30'))
    todo.add_task(Task('Call mom', '', None))

    while True:
        print("\nToDo CLI — choose option:")
        print("1) List all tasks")
        print("2) List incomplete tasks")
        print("3) Add task")
        print("4) Mark task complete")
        print("5) Exit")
        choice = input("Option: ").strip()

        if choice == '1':
            all_tasks = todo.list_all_tasks()
            if not all_tasks:
                print("No tasks.")
            for i, t in enumerate(all_tasks):
                print(f"{i}) {t}")

        elif choice == '2':
            inc = todo.list_incomplete_tasks()
            if not inc:
                print("No incomplete tasks.")
            for i, t in enumerate(inc):
                print(f"{i}) {t}")

        elif choice == '3':
            title = input("Title: ").strip()
            desc = input("Description (optional): ").strip()
            due = input("Due date (YYYY-MM-DD) or leave empty: ").strip()
            due = due if due else None
            task = Task(title, desc, due)
            todo.add_task(task)
            print("Task added.")

        elif choice == '4':
            all_tasks = todo.list_all_tasks()
            for i, t in enumerate(all_tasks):
                print(f"{i}) {t}")
            idx = input("Enter index to mark complete: ").strip()
            if idx.isdigit() and todo.mark_task_complete(int(idx)):
                print("Marked complete.")
            else:
                print("Invalid index.")

        elif choice == '5':
            print("Bye.")
            break
        else:
            print("Invalid option. Choose 1-5.")

if __name__ == '__main__':
    main()

# 2
# blog_app.py
# Simple CLI Blog system
# Run: python blog_app.py

from datetime import datetime

class Post:
    def __init__(self, title, content, author, created_at=None):
        """
        Post class:
        - title: string
        - content: string
        - author: string
        - created_at: datetime
        """
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at or datetime.now()

    def edit(self, new_title=None, new_content=None):
        if new_title:
            self.title = new_title
        if new_content:
            self.content = new_content
        # update timestamp
        self.created_at = datetime.now()

    def __str__(self):
        time = self.created_at.strftime('%Y-%m-%d %H:%M')
        return f"{self.title} by {self.author} at {time}\n{self.content[:80]}{'...' if len(self.content)>80 else ''}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def list_posts(self, latest_first=True):
        return sorted(self.posts, key=lambda p: p.created_at, reverse=latest_first)

    def posts_by_author(self, author):
        return [p for p in self.posts if p.author.lower() == author.lower()]

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            return True
        return False

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
            return True
        return False


def main():
    blog = Blog()
    # sample posts
    blog.add_post(Post('Welcome', 'This is the first post', 'Admin'))
    blog.add_post(Post('Python tips', 'Use list comprehensions...', 'Samandar'))

    while True:
        print("\nBlog CLI — choose option:")
        print("1) List all posts")
        print("2) Add post")
        print("3) Show posts by author")
        print("4) Edit post")
        print("5) Delete post")
        print("6) Exit")
        choice = input("Option: ").strip()

        if choice == '1':
            posts = blog.list_posts()
            if not posts:
                print("No posts.")
            for i, p in enumerate(posts):
                print(f"{i}) {p}\n")

        elif choice == '2':
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            content = input("Content: ").strip()
            blog.add_post(Post(title, content, author))
            print("Post added.")

        elif choice == '3':
            name = input("Author name: ").strip()
            found = blog.posts_by_author(name)
            if not found:
                print("No posts by this author.")
            for i, p in enumerate(found):
                print(f"{i}) {p}\n")

        elif choice == '4':
            posts = blog.list_posts()
            for i, p in enumerate(posts):
                print(f"{i}) {p}\n")
            idx = input("Index to edit: ").strip()
            if idx.isdigit():
                new_title = input("New title (leave empty to keep): ").strip() or None
                new_content = input("New content (leave empty to keep): ").strip() or None
                if blog.edit_post(int(idx), new_title, new_content):
                    print("Edited.")
                else:
                    print("Invalid index.")
            else:
                print("Invalid input.")

        elif choice == '5':
            posts = blog.list_posts()
            for i, p in enumerate(posts):
                print(f"{i}) {p}\n")
            idx = input("Index to delete: ").strip()
            if idx.isdigit() and blog.delete_post(int(idx)):
                print("Deleted.")
            else:
                print("Invalid index.")

        elif choice == '6':
            print("Bye.")
            break

        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()

# 3
# bank_app.py
# Simple CLI Banking system
# Run: python bank_app.py

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        """
        Account:
        - account_number: unique int or string
        - holder_name: string
        - balance: float
        """
        self.account_number = str(account_number)
        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False
        # simple overdraft handling: prevent negative balance
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"Account {self.account_number}: {self.holder_name} — Balance: {self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        if account.account_number in self.accounts:
            return False
        self.accounts[account.account_number] = account
        return True

    def get_account(self, account_number):
        return self.accounts.get(str(account_number))

    def transfer(self, from_acc, to_acc, amount):
        a = self.get_account(from_acc)
        b = self.get_account(to_acc)
        if a is None or b is None:
            return False, "One of accounts not found"
        if amount <= 0:
            return False, "Invalid amount"
        if a.balance < amount:
            return False, "Insufficient funds"
        a.withdraw(amount)
        b.deposit(amount)
        return True, "Transfer successful"

    def list_accounts(self):
        return list(self.accounts.values())


def main():
    bank = Bank()
    # sample accounts
    bank.add_account(Account(1001, 'Alice', 500.0))
    bank.add_account(Account(1002, 'Bob', 1000.0))

    while True:
        print("\nBank CLI — choose option:")
        print("1) Add account")
        print("2) Check balance / show account")
        print("3) Deposit")
        print("4) Withdraw")
        print("5) Transfer")
        print("6) List accounts")
        print("7) Exit")
        choice = input("Option: ").strip()

        if choice == '1':
            acc_no = input("Account number: ").strip()
            name = input("Holder name: ").strip()
            bal = input("Initial balance (optional): ").strip()
            bal = float(bal) if bal else 0.0
            acc = Account(acc_no, name, bal)
            if bank.add_account(acc):
                print("Account added.")
            else:
                print("Account exists.")

        elif choice == '2':
            acc_no = input("Account number: ").strip()
            acc = bank.get_account(acc_no)
            if acc:
                print(acc)
            else:
                print("Not found.")

        elif choice == '3':
            acc_no = input("Account number: ").strip()
            acc = bank.get_account(acc_no)
            if not acc:
                print("Not found.")
                continue
            amt = float(input("Amount to deposit: ").strip())
            if acc.deposit(amt):
                print("Deposited.")
            else:
                print("Invalid amount.")

        elif choice == '4':
            acc_no = input("Account number: ").strip()
            acc = bank.get_account(acc_no)
            if not acc:
                print("Not found.")
                continue
            amt = float(input("Amount to withdraw: ").strip())
            if acc.withdraw(amt):
                print("Withdrawn.")
            else:
                print("Insufficient funds or invalid amount.")

        elif choice == '5':
            a_from = input("From account number: ").strip()
            a_to = input("To account number: ").strip()
            amt = float(input("Amount to transfer: ").strip())
            ok, msg = bank.transfer(a_from, a_to, amt)
            print(msg)

        elif choice == '6':
            for a in bank.list_accounts():
                print(a)

        elif choice == '7':
            print("Bye.")
            break

        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()

