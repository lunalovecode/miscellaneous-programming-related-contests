portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("\nEnter the percent of your salary to save, as a decimal: "))
total_cost = float(input("\nEnter the cost of your dream home: "))
monthly_salary = annual_salary / 12
months = 0

while current_savings <= total_cost * portion_down_payment:
    current_savings += current_savings * (r / 12)
    current_savings += monthly_salary * portion_saved
    months += 1

print(f"\nNumber of months: {months}")
