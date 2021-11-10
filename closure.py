def make_multipier(x):
    
    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multipier(10)
times4 = make_multipier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))
      