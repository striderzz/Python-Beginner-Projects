def main():
  print("This is a monthly payment loan calculator")
  print("")

  principal = float(input("Input the loan amount: "))
  apr = float(input("Input the annual interest rate: "))
  years = int(input("Input amout of years: "))

  monthly_interest_rate = apr / 1200
  months = years * 12