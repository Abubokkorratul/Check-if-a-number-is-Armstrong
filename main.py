n = int(input("Enter a number: "))
sum_of_powers = sum(int(digit) ** len(str(n)) for digit in str(n))
if sum_of_powers == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
