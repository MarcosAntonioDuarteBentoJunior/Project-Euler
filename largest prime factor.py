
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


largest_prime_factor = 2


for i in range(2, 600851475143):
    if 600851475143 % i == 0 and is_prime(i) and i >= largest_prime_factor:
        largest_prime_factor = i

    print(largest_prime_factor,"     ", i)
else:
    print(largest_prime_factor)
