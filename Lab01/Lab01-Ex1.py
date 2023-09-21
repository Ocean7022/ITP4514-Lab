lowerNumber = int(input('Input the lower bound of prime numbers: '))
upperNumber = int(input('Input the upper bound of prime numbers: '))

def chkprime(number):
    if number < 2:
        print(number, 'is not a prime')
        return False
    else:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                return False
        return True


print('Prime numbers between', lowerNumber, 'and', upperNumber, 'are:')
for i in range(lowerNumber, upperNumber + 1):
    if chkprime(i):
        print(i)
