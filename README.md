# FizzBuzz solved in 3 lines | Python
***[Click here to acess the Python file](https://github.com/wallacewi/fizzbuzz-python/blob/main/fizzbuzz.py)***

### English
> This problem was solved thanks to the simplicity of the Python language.
> The `fizzbuzz` function in Python has a very simple code, with only 2 lines to test the number, and one more `return` to return the result depending on whether it meets or the requirements of the if statement.

***

### Português
> Esse problema foi resolvido graças a simplicidade da linguagem Python.
> A função em Python `fizzbuzz` possui um código bastante simples, com apenas 2 linhas para testar o número, e mais uma `return` para retornar o resultado dependendo se atende ou os requisitos das if declaradas.

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
***Awesome! [Click here to acess Python file](https://github.com/wallacewi/fizzbuzz-python/blob/main/fizzbuzz.py)*** <br>
> *Want to know how this works, watch this explanation: [link to YouTube [English]](https://youtu.be/QPZ0pIK_wsc)*
