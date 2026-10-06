# EXPENSE TRACKER - INSTALLMENT 1
# Author : Harvey Sanico
# A simple personal expense tracher program. 

print("=" * 40)
print("          EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)

print()
print("Welcome! This is your personal expense tracker.")
print()


print("MAIN MENU")
print("[1] Add an expense       (coming soon)")
print("[2] View all expenses    (coming soon)")
print("[3] Show total spent     (coming soon)")
print("[4] Exit                 (coming soon)")

print("-" * 40)
print("Made by: Harvey Sanico | Installmentt 1")
print("=" * 40)

# Expense Tracker - Installment 2

# Lab 1 banner and menu

name = input("What is your name? ")

print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("Enter first expense item: ")
amount1 = float(input("Enter amount: "))

item2 = input("Enter second expense item: ")
amount2 = float(input("Enter amount: "))

total = amount1 + amount2
average = total / 2

print("----------------------------------------")
print("SUMMARY")
print(f"-{item1:<20} ${amount1:>10.2f}")
print(f"-{ item2:<20} ${amount2:>10.2f}")
print(f"{' Total Spent:':<20} ${total:>10.2f}")
print(f"{' Average:':<20} ${average:>10.2f}")
print("----------------------------------------")

print(f"Made by: {name} | Installment 2")


