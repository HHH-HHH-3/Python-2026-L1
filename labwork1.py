def ex1():
rad = input("Enter circle radius:")
area = 3.14 * float(rad) **2
print(f"Circle area: {area}")

def ex2():
temp = input("Enter the temperature in Celsius:")
result = (float(temp) *9/5) + 32
print(f" {temp} (C) = {result} (F)")

def ex3():
num = int(input("Enter a number? "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

def ex4():
    number = int(input("Enter a number: "))
   
    if number > 1:
        divisor_sum = sum(
            divisor
            for divisor in range(1, number)
            if number % divisor == 0
        )
    else:
        divisor_sum = 0

    if divisor_sum == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

def ex5()
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white"]
favorite_color = input("What is your favorite color? ").strip().lower()

if favorite_color in colors:
	print(colors.index(favorite_color))
else:
	print("Sorry, I could not find your color")

def ex6():
print(list(range(6)))

print(list(range(1, 11, 3)))

print(list(range(5, 0, -1)))

print(list(range(6, -4, -2)))

def ex7():
def remove_dollar_sign(s):
    return s.replace("$", "")

s = input("Enter a string: ")
result = remove_dollar_sign(s)
print("String without dollar sign:", result)

def ex8():
def extract_even(l):
	return [number for number in l if number % 2 == 0]

l = [1, 4, 5, -1 , -10]
output = extract_even(l)
print(output)

def ex9():
def calculate_factorial(x):
    res = 1
    for i in range(1, int(x) + 1):
        res *= i
    return res

x = int(input("Enter a number:"))
factorial = calculate_factorial(x)
print(f"The factorial of {x} is: {factorial}")
    
def ex10():
def calculate_divisors(n):
    sorted_divisors = sorted([i for i in range(1, n + 1) 
                              if n % i == 0])
    return sorted_divisors

n = int(input("Enter a number:"))
divisors = calculate_divisors(n)
print(f"The divisors of {n} are: {divisors}")

def ex11():
a = list(map(int, input().split()))
print(f"{((a[2]- a[0]) ** 2 + (a[3] - a[1]) ** 2) ** 0.5:.2f}")

def ex12():
 m, n = map(int, input().split())
print("*" * m)
for i in range(1, n + 1 - 2):
    print("*" + " " * (m - 2) + "*")
    print("*" * m)    
