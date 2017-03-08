def fizz_buzz(num):#creating the function

    a='Fizz'
    b='Buzz'
    c='FizzBuzz'

    if (num%3==0) and (num%5==0):#checking for the conditions.
        return c
    elif (num%5==0):
        return b
    elif (num%3==0) :
        return a
    else:
        return num