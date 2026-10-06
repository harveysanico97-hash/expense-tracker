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

# Expense Tracker - Installment 2

# Lab 1 banner and menu

name = input("What is your name? ")

print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("Enter first expense item: ")
amount1 = float(input("Enter amount: "))
subtotal = subtotal + amount1

item2 = input("Enter second expense item: ")
amount2 = float(input("Enter amount: "))
subtotal = subtotal + amount2


average = subtotal / 2

tax_rate = int(input("Enter tax rate: "))
tax = subtotal * tax_rate / 100
grand_total = subtotal + tax 


budget = float(input("Enter your budget: "))
over_budget = grand_total > budget
left_in_budget = budget - grand_total

print("----------------------------------------")
print("SUMMARY")
print(f"{item1}:\t$ {amount1:.2f}")
print(f"{item2}:\t$ {amount2:.2f}")
print(f"Subtotal:\t$ {subtotal:.2f}")
print(f"Average:\t$ {average:.2f}")
print(f"Tax ({tax_rate}%):\t$ {tax:.2f}")
print(f"Grand total:\t$ {grand_total:.2f}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t$ {left_in_budget:.2f}")
print("----------------------------------------")
print(f"Made by: {name} | Installment 3")


