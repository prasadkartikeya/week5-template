def greet(name):
    return f"Hello, {name}!"


def sum_of_two(x, y):
    return x + y


def max_of_three(a, b, c):
    return max(a, b, c)


def factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_vowels(text):
    return sum(1 for ch in text if ch.lower() in "aeiou")








    
    


        
    













    



    




