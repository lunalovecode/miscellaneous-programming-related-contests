portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("\nEnter the percent of your salary to save, as a decimal: "))
total_cost = float(input("\nEnter the cost of your dream home: "))
semi_annual_raise = float(input("\nEnter the semiannual raise, as a decimal: "))

monthly_salary = annual_salary / 12
months = 0

while current_savings <= total_cost * portion_down_payment:
    current_savings += current_savings * (r / 12)
    current_savings += monthly_salary * portion_saved
    months += 1
    if months % 6 == 1 and months > 6:
        monthly_salary += monthly_salary * semi_annual_raise

print(f"\nNumber of months: {months}")