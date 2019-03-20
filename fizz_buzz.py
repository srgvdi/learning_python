def fizz_buzz(n):
    for number in range(1, n):
        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 5 == 0:
            print('buzz')
        else:
            print(number)
    return


print(fizz_buzz(105))
