def perfect(n):
    divisors=[i for i in range (1,n) if n%i==0]
    return sum(divisors)==n
def pefect(limit):
    perfect_numbers=[]
    for num in range(2,limit):
        if perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers
perfect_numbers=perfect(1000000)
print("the perfect numbers are:",perfect_numbers)