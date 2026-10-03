# Project: Expense Tracker
# Installment: 3
# Author: Shaheena H. Muctar
# Description: A simple personal expense tracker

print("=" * 40)
print("    EXPENSE TRACKER")
print("    Know where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("    [1] Add an expense      (coming soon)")
print("    [2] View all expenses   (coming soon)")
print("    [3] Show total spent    (coming soon)")
print("    [4] Exit                (coming soon)")

print()

name = input("What is your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

item1 = input("Enter the first expense item: ")
amount1 = float(input(f"Enter the amount spent on {item1}: $"))

subtotal = 0
subtotal = subtotal + amount1

item2 = input("Enter the second expense item: ")
amount2 = float(input(f"Enter the amount spent on {item2}: $"))

subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = int(input("Enter the tax rate (%): "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Enter your budget: $"))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent:.1f}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print()
print(f"Made by: {name} | Installment 3")
print("=" * 40)