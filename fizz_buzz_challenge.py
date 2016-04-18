def fizz_buzz(value):
    if value % 15 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return value


def challenge():
    for x in range(1, 101):
        print fizz_buzz(x)
