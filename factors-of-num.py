def factors(n):
    fac = []
    for x in range(1,n+1):
        if n%x == 0:
            fac.append(x)
    return fac
n = int(input("Enter the number: "))
factor_list = factors(n)
print("Factors of {} are: ".format(n))
print (str(factor_list)[1:-1])
