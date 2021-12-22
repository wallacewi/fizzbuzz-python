def fizzbuzz(n):
    fizz = True if n % 3 == 0 else False
    buzz = True if n % 5 == 0 else False
    return 'Fizz Buzz' if fizz and buzz else 'Fizz' if fizz else 'Buzz' if buzz else n


# teste
num = fizzbuzz(int(input('Digite um número: ')))
print(num)
