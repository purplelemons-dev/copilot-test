
class Factorial:
    def __init__(self, n):
        self.n = n
        self.ints=[i for i in range(2,n+1)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        else:
            self.n -= 1
            return self.n * self.__next__()
    
    def __str__(self):
        return str(self.n)
    
    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        total=1
        for i in self.ints:
            total*=i
        return total

def divide(dividend:Factorial, divisor:Factorial):
    if len(divisor.ints) > len(dividend.ints):
        raise ValueError("Divisor is larger than dividend")
    quotient=1
    for i in range(divisor.ints[-1]+1, dividend.ints[-1] + 1):
        quotient*=i
    return quotient
