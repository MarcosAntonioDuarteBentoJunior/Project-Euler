
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


term = 1
sum = 0

while True:
    if fibonacci(term) > 4000000:
        break

    if isEven(fibonacci(term)):
        sum += fibonacci(term)

    term += 1


print(sum)
