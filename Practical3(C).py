<<<<<<< HEAD
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):
    if n > 1:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
=======
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):
    if n > 1:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
>>>>>>> 74749572667462e54cbe4527c6342a979a9c1499
            print(n, end=" ")