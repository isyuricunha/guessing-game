print('********************************')
print('Welcome to the Guessing Game!')
print('********************************')

secretNumber = 42

shot = input('Put your number: ')

print('You put the number', shot)

shot = int(shot)

if secretNumber == shot:
    print('You won')
else:
    print('You lose.')
