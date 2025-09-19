import cmath

a = 1
b = -2
c = 3

def root(a,b,c):
    judge = b ** 2 - 4 * a * c 

    if judge > 0:
        r1 = (-b + cmath.sqrt(judge)) / (2*a)
        r2 = (-b - cmath.sqrt(judge)) / (2*a)
        return r1, r2
    elif judge == 0:
        r1 = -b / (2*a)
        r2 == r1
        return r1, r2
    else :
        real = -b / 2*a
        imag = cmath.sqrt(judge) / (2*a)
        r1 = f"{real} + {imag}"
        r2 = f"{real} - {imag}"
    print("Root 1 = ", r1)
    print("Root 2 = ", r2)

root(a,b,c)
