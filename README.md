# FizzBuzz solved in 3 lines - Python solution
***[Click here to acess the Python file](https://github.com/wallacewi/fizzbuzz-python/blob/main/fizzbuzz.py)***

### About
> This problem was solved thanks to the simplicity of the Python language. As you will see below, I had to follow a few steps to get to the final code result.

This script works like this:

If the number is only divisible by 3, the function will return 'Fizz'. If the number is divisible only by 5, the function returns 'Buzz'. If the number is divisible by 3 and 5, the function returns 'FizzBuzz'.

So the `fizzbuzz()` function takes a one-number instruction and returns four possible results.

## Learn the steps to simplify
1. Initial code
```
def fizzbuzz(n):
    fizz = False 
    buzz = False
    if n % 3 == 0:
        fizz = True
    if n % 5 == False:
        buzz = True
    if fizz == True and buzz == True:
        return 'FizzBuzz'
    elif fizz == True and buzz == False:
        return 'Fizz'
    elif fizz == False and buzz == True:
        return 'Buzz'
    else:
        return n
```
2. Reformat the script correctly
```
def fizzbuzz(n):
    fizz = False 
    buzz = False
    if n % 3 == 0:
        fizz = True
    if n % 5 == False:
        buzz = True
    if fizz and buzz:
        return 'FizzBuzz'
    elif fizz and not buzz:
        return 'Fizz'
    elif not fizz and buzz:
        return 'Buzz'
    else:
        return n
```
3. Siplify the if statement of `fizz` and `buzz`
```
def fizzbuzz(n):
    fizz = True if n % 3 == 0 else False
    buzz = True if n % 5 == 0 else False
    if fizz and buzz:
        return 'FizzBuzz'
    elif fizz and not buzz:
        return 'Fizz'
    elif not fizz and buzz:
        return 'Buzz'
    else:
        return n
```
4. Finally, simplify if statements into a single `return`
```
def fizzbuzz(n):
    fizz = True if n % 3 == 0 else False
    buzz = True if n % 5 == 0 else False
    return 'Fizz Buzz' if fizz and buzz else 'Fizz' if fizz else 'Buzz' if buzz else n
```
***Awesome! [Click here to acess Python file](https://github.com/wallacewi/fizzbuzz-python/blob/main/fizzbuzz.py)***

> *Want to know how this works, watch this explanation: [link to YouTube [English]](https://youtu.be/QPZ0pIK_wsc)*
