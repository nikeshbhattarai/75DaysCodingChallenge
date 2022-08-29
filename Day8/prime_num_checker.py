def prime_checker(number):
    is_prime = True
    print("yeha")
    for i in range(2, number):
        print(i)
        if number % i == 0:
            is_prime = False
    print("2 ma chaldaina")
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} isnot a prime number.")

n = int(input("Enter a number: "))
prime_checker(number=n)