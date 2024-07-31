# calculator.py

def calculate_monthly_payment(principal, annual_rate, years):
    # 将年利率转换为月利率
    monthly_rate = annual_rate / 12 / 100
    # 计算总还款期数
    total_payments = years * 12
    # 计算每月还款额
    if monthly_rate == 0:  # 无利率的情况
        return principal / total_payments
    else:
        return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)

def main():
    print("Welcome to the Loan Calculator!")

    try:
        principal = float(input("Enter the loan amount: "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    print(f"Your monthly payment is: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
