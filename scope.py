# Local scope

def local():
    x = 300
    print('x is', x)

# Global scopeß

y = 200

def globalfunc():
    print('y is', y)

def my_other_globalfunc():
    print('y is', y)

# snippet

z = 5
    
def snippet():
    z = 10
    print('z is', z)


# snippet2

z = 5

def snippet2():
    z = 10

    def my_other_func():
        z = 15
        print('z is', z)

    my_other_func()
    print('z is', z)

    
def main():
    local()
    y = 200
    globalfunc()
    my_other_globalfunc()
    z = 5
    snippet()
    print('z is', z)
    snippet2()
    print('z is', z)
    
    

if __name__ == '__main__':
   main()
