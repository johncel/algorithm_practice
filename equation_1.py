# Write a functison that parses and evaluates an arithmetic string
# Ex. "1+2", "1*2*3*4*5", "34-5*100", "10-20*30+40/50"
# Positive integers separated by +, -, * or /. No parentheses
# You must respect the order of operations: *, / take precedence over +, -
# You have 30 minutes. Good luck!

# str = "1+2*3"
str = "10-20*30+40/50"

def simplify_equation(ops, toks):
    left_ops = []
    right_ops = []
    
    left_toks = []
    right_toks = []

    i = 0
    for op in ops:
        left = float(toks[i])
        right = float(toks[i+1])
        if op == '*':
            res = left * right
            toks[i+1] = res
            toks = toks[0:i] + [res] + toks[i + 2:]
            ops = ops[0:i] + ops[i+1:]
            return toks, ops
        if op == '/':
            res = left / right
            toks[i+1] = res
            toks = toks[0:i] + [res] + toks[i + 2:]
            ops = ops[0:i] + ops[i+1:]
            return toks, ops
        i = i + 1

    return toks, ops

        
# parse into toks (numbers) and operations
tok = ''
ops = []
toks = []
for char in str:
    if char.isdigit():
        tok = tok + char
    else:
        toks.append(tok)
        ops.append(char)     
        tok = ''
toks.append(tok)

# perform all * and / first
while '*' in ops or '/' in ops:
    toks, ops = simplify_equation(ops, toks)

# finish up by performing the + /
final_result = float(toks[0])
i = 0
for op in ops:
    if op == '+':
        final_result = final_result + float(toks[i+1])
    if op == '-':
        final_result = final_result - float(toks[i+1])
    i = i + 1

print(f'{str} has result {final_result}')
