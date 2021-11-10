import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter ==0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux
        

if __name__ == '__main__':
    num = int(input("Ingrese el numero de elementos de la sucesion: "))
    fibonacci = fibo_gen()
    for i in fibonacci:
        if  i < num:
            print(i)
            time.sleep(0.05)
        else:
            break
