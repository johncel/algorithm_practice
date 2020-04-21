def f(x, l=[], foo=['b', 'a', 'r']):
    for i in range(x):
        l.append(i*i)
    print(l)
    print(foo)
    foo = ['s', 'a', 'l']

f(2)

f(3, [3,2,1])

f(3)
