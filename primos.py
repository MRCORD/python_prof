
#funcion para identificar si un numero es primo con list comprehension
#estamos usando tipados estaticos
#mypy

def es_primo(num:int) -> bool:
    return len([x for x in range(2,num) if num % x == 0]) == 0

def main():
    input_num = int(input("Ingrese un numero: "))
    print(f"El numero {input_num} es primo: {es_primo(input_num)}")
          
if __name__ == '__main__':
    main()