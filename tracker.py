# Project: Expense Tracker
# Installment: 2
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

item1 = input("Enter the first expense: ")
amount1 = float(input("Enter the amount: "))

item2 = input("Enter the second expense: ")
amount2 = float(input("Enter the amount: "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print(f"{item1}: ${amount1}")
print(f"{item2}: ${amount2}")
print(f"Total spent: ${total}")
print(f"Average: ${average}")
print("-" * 40)
print("Made by: Shaheena H. Muctar | Installment 2")
