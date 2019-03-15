def is_perfect(number):
    sum_of_divisors = 1
    i = 2
    while i < number:
        if number % i == 0:
            sum_of_divisors += i
        i += 1
    return True if sum_of_divisors == number and number != 1 else False


limit = int(input("Enter a number"))
print("Below are all perfect numbers till 10000")
n = 2
for n in range(limit):
    if is_perfect(n):
        print(n, " is a perfect number")
