# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def find_all_div(number):
    div_list = []
    divider = 2
    while divider <= number:
        if number % divider == 0:
            div_list.append(divider)
        divider += 1
    return div_list 

def prime_factor_decomposition(number):
    a = find_all_div(number)
    b = []
    prime_factor = a[0]
    b.append(prime_factor)
    if prime_factor == number:
        return b
    b += prime_factor_decomposition(number / a[0])
    return b
number = 362312
dec = prime_factor_decomposition(number)
for n in dec:
     while dec.count(n) > 1:
        dec.remove(n)   
print(f"{dec} - список простых множителей числа {number}")
    


