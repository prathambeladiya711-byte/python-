n = int(input("enter num"))

a,b= 0,1

i = 0

while i < n:
    print(a)
    c = a+b
    a = b
    b = c 
    i += 1
    
