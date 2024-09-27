def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    if n > 2:
        factors[n] = 1
    return factors
def calculate_weighted_sum(arr, num):
    if not arr:
        return -1
    factors = prime_factors(num)
    total_sum = 0
    found = False
    for factor, power in factors.items():
        if factor < len(arr):
            total_sum += power * arr[factor]
            found = True
    return total_sum if found else 0
if __name__== "__main__":
    import sys
    n = int(input())
    arr = list(map(int,input().split()))
    num = int(input())
    result = calculate_weighted_sum(arr, num)
    print(result)