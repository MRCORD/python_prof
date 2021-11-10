import time

class FiboIter():
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
            
# 0 1 1 2 3 5 8 13 21 34 55

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    
    fibonacci = FiboIter()
    for i in fibonacci:
        if i < n:
            print(i)
            time.sleep(0.05)
        else:
            break