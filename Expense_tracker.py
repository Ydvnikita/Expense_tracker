total = 0

print("Expense Tracker")
print("Type 'quit' to stop")

while True:
    expense = input("Enter expense amount: ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)
        total += expense
        print("Current Total:", total)
    except ValueError:
        print("Invalid Data! Please enter a number.")

print("\nFinal Total Spent:", total)