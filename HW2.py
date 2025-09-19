import cmath

a = 1
b = -2
c = 3

def root(a,b,c):
    judge = b ** 2 - 4 * a * c 

    if judge != 0:
        r1 = (-b + cmath.sqrt(judge)) / (2*a)
        r2 = (-b - cmath.sqrt(judge)) / (2*a)
    elif judge == 0:
        r1 = -b / (2*a)
        r2 = r1
    return r1, r2
        
r1, r2 = root(a,b,c)
print("Root 1 = ", r1)
print("Root 2 = ", r2)

