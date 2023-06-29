import re

# The regular expression to match a valid email address.
regex = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'

# Get the email address from the user.
email = input("Enter an email address: ")

# Check if the email address is valid.
def check_email(email):
  """
  Check if the email address is valid.

  Args:
    email: The email address to check.

  Returns:
    True if the email address is valid, False otherwise.
  """

  # Use the `re.fullmatch()` method to match the regular expression.
  match = re.fullmatch(regex, email)

  # Check if the email address makes sense.
  if match and not email.split('@')[0].isalpha():
    return False

  # Check if the email address is a real combination of names.
  if match and not email.split('@')[0].split('.')[0].isalpha():
    return False

  return match

# Check if the email address is valid and print the result.
if check_email(email):
  print("The email address is valid.")
else:
  print("The email address is invalid.")
