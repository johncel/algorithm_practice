x = 1 
print(x)

x = 1 << 1 
print(x)

x = 255 >> 1
print(x)

x = 1 << 7
print(x)

x = 1 << 8
print(x)

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)
def bin2(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

for x in [1,2,3,11,32,255,256]:
    y = bin(x)
    print(f'x={x} bin(x)={y}')
    y = bin2(x)
    print(f'x={x} bin2(x)={y}')
