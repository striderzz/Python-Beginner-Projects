def main():
  print("Welcome to the email slicer")
  print("")

  email_input = input("Input your email address: ")

  (username,domain) = email_input.split("@")
  (domain,extension) = domain.split(".")

  print(f'Username: {username}, Domain: {domain}, Extension: {extension}.')

main()