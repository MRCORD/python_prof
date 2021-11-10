#Hola 3 -> HolaHolaHola
#Facundo 2 -> FacundoFacundo
#Platzi 4 -> PlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(s):
        assert type(s) == str, 'Solo puedes usar string'
        return s * n
    return repeater


#This closure returns a function that returns the division of an x number by n

def make_division_by(n):
    def division(x):
        assert type(x) == int, 'Solo puedes usar int'
        return x / n
    return division

def main():
    repeat5 = make_repeater_of(5)
    print(repeat5('Hola'))
    
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    
    division_by_18 = make_division_by(18)
    print(division_by_18(54))
    
if __name__ == '__main__':
    main()