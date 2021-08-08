def fact(n):
    # assuming that n is a positive integer or 0
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

# print("0! =", fact(0))
while True:
    print(fact(int(input("Enter a number: "))))
