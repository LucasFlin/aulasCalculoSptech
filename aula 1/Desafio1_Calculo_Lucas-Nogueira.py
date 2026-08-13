def fibonacci_par_impar():
    n1 = 0
    n2 = 1
    n3 = 1

    while n2 <= 21:
        n2 = n3
        if n2 % 2 == 0:
            print(f'{n2} é par')
        else:
            print(f'{n2} é impar')
        n3 = n1+n2
        n1 = n2

fibonacci_par_impar()