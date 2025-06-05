#my first machine learning project#
prime_number = int(input("Enter a number: "))
if prime_number > 1:
    for i in range(2, prime_number):
        if (prime_number % i) == 0:
            print(prime_number, "is not a prime number")
            break
    else:
        print(f"{prime_number} is a prime number")
else:
    print(f"{prime_number} is not a prime number")

#fizzbuzz
user_input = int(input("enter a number: "))
if user_input % 3 == 0 and user_input % 5 == 0:
    print('fizzbuzz')
elif user_input % 3 == 0:
    print('fizz')
elif user_input % 5 == 0:
    print('buzz')
else:
    print(f"{user_input} not divisible by 5 and 3")

# random number guessing game
