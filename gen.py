import time


def slow_gen(n):
    for i in range(0,n):
        yield i
        time.sleep(2)

numbers = slow_gen(10)

for i in numbers:
    print(f'numbers contains {i}')
