numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
exeption = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

# get valid input
valid = False
while valid == False:
    user = input("enter number to convert: ")
    if user.isdigit():
        user = int(user)
        valid = True
    else:
        print("Invalid input, must be number...")

converted = []
number = 0

# convert
for i in numbers:
    # check if exeption
    for j in exeption:
        if user == j:
            converted.append(exeption[j])
            user -= j
            continue

    if numbers[i] <= user:
        converted.append(i)
        number = numbers[i]

        while number + numbers[i] <= user:
            converted.append(i)
            number += numbers[i]

        user -= number



result = "".join(converted)
print(result)
