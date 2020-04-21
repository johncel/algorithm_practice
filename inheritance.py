
class base_class():
    def __init__(self, a):
        self.a = a

    def go(self, x):
        print(x*self.a)

class base_class_2():
    def __init__(self, c):
        self.c = c

    def go(self, x):
        print(x*self.a)

class child_class(base_class):
    def __init__(self, a, b):
        super(child_class, self).__init__(a)
        self.b = b

    def go(self, x,y):
        super(child_class, self).go(x)
        print(y*self.b)

class child_class_2(base_class, base_class_2):
    def __init__(self, a, b, c):
        super(child_class_2, self).__init__(a)
        self.b = c

    def go(self, x,y,z):
        super(child_class_2, self).go(x)
        print(y*self.b)


bc = base_class(10)
bc.go(5)


cc = child_class(10, 20)
cc.go(5,15)

ccc = child_class_2(10, 20, 30)
ccc.go(5,15,25)
