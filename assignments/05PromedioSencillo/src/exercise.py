def promedio(x):
    i = 1
    num = 0
    suma = 0
    while i <= x:
        num = float(input())
        suma += num
        i += 1
    return suma/x 
    
def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    prom = promedio(n)
    print(prom)

if __name__=='__main__':
    main()
