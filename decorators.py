from datetime import datetime

def execution_time(func): 
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time_diff = end - start
        print(f"Execution time: {time_diff.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass
       
@execution_time
def suma(a:int, b:int) -> int:
    return a + b

@execution_time
def saludo():
    print("Hola")

random_func()
suma(1,2)
saludo()