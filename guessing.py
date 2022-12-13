print('********************************')
print('Welcome to the Guessing Game!')
print('********************************')

secretNumber = 42  # The number you need to discover.

guessing = input('Put your number: ')  # For request a number.

print('You put the number', guessing)  # For show the select number.

guessing = int(guessing)  # Here we transform the variable `guessing` to inter, because before of this, is a str (string). You can
# see this with type(guessing) in terminal.

if secretNumber == guessing:  # A logic to recognize if it is a correct number or not
    print('You won')
else:
    print('You lose.')

# I hope you can guess the number... Or not.
