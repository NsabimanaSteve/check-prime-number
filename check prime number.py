
def isprime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
    return True
def main():
    value=int(input('Enter an integer: '))
    if isprime(value):
        print(value,'is a prime.')
    else:
        print(value,'is not a prime.')

main()
    