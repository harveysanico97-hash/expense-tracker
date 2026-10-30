# EXPENSE TRACKER - INSTALLMENT 5
# Author : Harvey Sanico
# A simple personal expense tracker program.
 
print("...  (banner)  ...")
name = input("What's your name? ")
tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0
expense_count = 0 


print("\nMAIN MENU")
print("  [1] Add an expense")
print("  [2] View all expenses (coming soon)")
print("  [3] Show total spent")
print("  [4] Exit")

while True: 
 choice = input("Choose 1-4: ")

 if choice == "1":
     Amount = float(input("Amount? "))

     subtotal += Amount
     expense_count += 1 

     if Amount < 100:
         print("  Small expense.")
     else: 
        print("   Big expense.")

 elif choice == "2":
    print("   Coming soon: the tracker can't remember each item yet.")

 elif choice =="3":
    tax = subtotal * (tax_rate / 100)
    grand_total = subtotal + tax
    remaining = budget - grand_total 

    print(f"   Expreses:     {expense_count}")
    print(f"   Subtotal:     ${subtotal:.1f}")
    print(f"   Tax  ({tax_rate:.1f}%):     ${tax:.1f}")
    print(f"   Grand total:  ${grand_total:.1f}")

    if remaining >= 0: 
        print(f"   Careful: only ${remaining:.1f} left.")
    else:
        print(f"   Over budget by ${abs(remaining):.1f}.")

 elif choice == "4":
    print(f"Goodbye, {name}!")
    print("-" * 40)
    print("Made by: Harvey Sanico | Installment 5")
    print("=" *40)
    break

 else:
    print("   Please choose 1,2,3, or 4.")




