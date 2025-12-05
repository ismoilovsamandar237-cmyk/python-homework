from datetime import date

def days_in_month(year, month):
    # keyingi oy boshi - shu oy boshi = shu oy kunlari
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    this_month = date(year, month, 1)
    return (next_month - this_month).days

# 1. Foydalanuvchidan tug'ilgan sana
birth_str = input("Enter your birthdate (YYYY-MM-DD): ")  # masalan: 2005-03-15
by, bm, bd = map(int, birth_str.split("-"))
birth = date(by, bm, bd)

# 2. Bugungi sana
today = date.today()

# 3. Yil, oy, kun farqi
years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day

# Kun manfiy bo'lsa, bir oy "qarz" olib to'g'rilaymiz
if days < 0:
    months -= 1
    # oldingi oyning kunlari
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month != 1 else today.year - 1
    days += days_in_month(prev_year, prev_month)

# Oy manfiy bo'lsa, bir yil "qarz" olib to'g'rilaymiz
if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")

# 2
# from datetime import date

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
by, bm, bd = map(int, birth_str.split("-"))
today = date.today()

# Bu yilgi tug'ilgan kun
next_birthday = date(today.year, bm, bd)

# Agar bugun yoki o'tgan bo'lsa, keyingi yilga suramiz
if next_birthday <= today:
    next_birthday = date(today.year + 1, bm, bd)

delta = next_birthday - today
print(f"Days until your next birthday: {delta.days} days")

# 3
from datetime import datetime, timedelta

now_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Meeting duration hours: "))
minutes = int(input("Meeting duration minutes: "))

# Matndan datetime qilish
current_dt = datetime.strptime(now_str, "%Y-%m-%d %H:%M")

duration = timedelta(hours=hours, minutes=minutes)
end_dt = current_dt + duration

print("Meeting will end at:", end_dt.strftime("%Y-%m-%d %H:%M"))

# 4
from datetime import datetime, timedelta

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
src_offset = float(input("Your timezone offset from UTC (e.g. +5, -3): "))
dst_offset = float(input("Target timezone offset from UTC: "))

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

# Manba va maqsad offset farqi
offset_diff = dst_offset - src_offset
converted_dt = dt + timedelta(hours=offset_diff)

print("Converted date and time:", converted_dt.strftime("%Y-%m-%d %H:%M"))

# 5
from datetime import datetime
import time

target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if now >= target:
        print("Time is up!")
        break

    remaining = target - now
    # Kun, sekundlarni soat, minut, sekundlarga bo'lamiz
    total_seconds = int(remaining.total_seconds())
    days = total_seconds // 86400
    total_seconds %= 86400
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    print(f"Remaining: {days}d {hours}h {minutes}m {seconds}s", end="\r")
    time.sleep(1)

# 6
import re

email = input("Enter email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# 7
import re

phone = input("Enter phone number: ")

# faqat raqamlarni olib qolamiz
digits = re.sub(r"\D", "", phone)

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted:", formatted)
else:
    print("Invalid phone number (need 10 digits)")

# 8
import re

password = input("Enter password: ")

length_ok = len(password) >= 8
upper_ok = re.search(r"[A-Z]", password) is not None
lower_ok = re.search(r"[a-z]", password) is not None
digit_ok = re.search(r"\d", password) is not None

if length_ok and upper_ok and lower_ok and digit_ok:
    print("Strong password ✅")
else:
    print("Weak password ❌")
    print("Requirements:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")

# 9
import re

text = """
Python is great. I love python because Python is simple but powerful.
"""
word = input("Enter word to search: ")

pattern = rf"\b{re.escape(word)}\b"

matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))

if not matches:
    print("Word not found.")
else:
    print(f"Found {len(matches)} occurrence(s):")
    for m in matches:
        start = m.start()
        end = m.end()
        print(f"- From index {start} to {end}: '{text[start:end]}'")

# 10
import re

text = input("Enter text: ")

# dd/mm/yyyy yoki dd-mm-yyyy
pattern1 = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"
# yyyy-mm-dd
pattern2 = r"\b\d{4}-\d{2}-\d{2}\b"

dates = re.findall(pattern1, text) + re.findall(pattern2, text)

if dates:
    print("Found dates:")
    for d in dates:
        print("-", d)
else:
    print("No dates found.")









