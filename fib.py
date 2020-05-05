import time

class FibMem:
    def __init__(self):
        self.lookup = {}

    
    def f(self, n):
        if n in self.lookup:
            return self.lookup[n]
        if n < 2:
            return n
        else:
            res = self.f(n-1) + self.f(n-2)
            self.lookup[n] = res
            return res

class Fib:
    def f(self, n):
        if n < 2:
            return n
        else:
            res = self.f(n-1) + self.f(n-2)
            return res


fm = FibMem()
f = Fib()

start = time.time()
res = fm.f(40)
print(f' {res} memoization took {time.time() - start} seconds')
res = f.f(40)
print(f' {res} took {time.time() - start} seconds')
