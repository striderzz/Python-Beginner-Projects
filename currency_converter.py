def main():
  rate = 0.9
  print("This program converts US dollars to euro")
  print()

  dollars = int(input("Enter currency in dollars: "))

  euro_conversion = round(rate * dollars)

  print(f'The converted currency in euro: {euro_conversion} ')

main()  