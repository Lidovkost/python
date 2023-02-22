number = abs(int(input('введите число ')))
b = 0
while number != 0:
    if b < number % 10:
        b = number % 10
    if b == 9:
        break
    number = number//10
text = f'самая большая цифра в числе = {b}'
print(text)
