def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
        return True
def count_primes_between(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count +=1
    return count
def nth_prime(n):
    if n<1:
        return -1
    
    count = 0 
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
    return -1

def is_twin_prime(n):
    return is_prime(n) and is_prime(n+2)

print("Prime NUmber Analysis")
print("=" * 40)

count1 = count_primes_between(1, 50)
print(f"The numbers between 1 and 50: {count1}")

prime10 = nth_prime(10)
print(f"The 10th prime number is: {prime10}")

num1 = 11
twin1 = is_twin_prime(num1)
print(f"Is {num1} part of a twin prime pair? {twin1}")
if twin1:
    print(f"  Twin pair: ({num1}, {num1 + 2}")

num2 = 15
twin2 = is_twin_prime(num2)
print(f"Is {num2} part of a twin prime pair? {twin2}")
if twin2:
    print(f"  Twin pair: ({num2}, {num2 + 2})")

num3 = 29
twin3 = is_twin_prime(num3)
print(f"Is {num3} part of a twin prime pair? {twin3}")
if twin3:
    print(f"  Twin pair: ({num3}, {num3+2})")

count2 = count_primes_between(100, 150)
print(f"\nPrime numbers between 100 and 150: {count2}")