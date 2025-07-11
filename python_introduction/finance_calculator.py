Monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
Monthly_savings = Monthly_income - monthly_expenses
print("Your projected monthly savings are:", Monthly_savings)
print("Your projected annual savings are:", Monthly_savings * 12 + (Monthly_savings *12 * 0.05))
