print('********************************')
print('Welcome to the Guessing Game!')
print('********************************')

secretNumber = 42  # The number you need to discover.

shot = input('Put your number: ')  # For request a number.

print('You put the number', shot)  # For show the select number.

shot = int(shot)  # Here we transform the variable `shot` to inter, because before of this, is a str (string). You can
# see iso with type(shot) in terminal.

if secretNumber == shot:  # A logic to recognize if it is a correct number or not
    print('You won')
else:
    print('You lose.')

# I hope you can guess the number... Or not.
