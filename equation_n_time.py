# Write a functison that parses and evaluates an arithmetic string
# Ex. "1+2", "1*2*3*4*5", "34-5*100", "10-20*30+40/50"
# Positive integers separated by +, -, * or /. No parentheses
# You must respect the order of operations: *, / take precedence over +, -
# You have 30 minutes. Good luck!

# str = "1+2*3"
str = "10-20*30+40/50"
        
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
# writing a new simpler equation in terms of ops and toks
ops_simple = []
toks_simple = [toks[0]]
i = 0
for op in ops:
    if ops[i] == '*':
        result = float(toks[i]) * float(toks[i+1])
        toks_simple[-1] = result
    elif ops[i] == '/':
        result = float(toks[i]) / float(toks[i+1])
        toks_simple[-1] = result
    else:
        ops_simple.append(op)
        toks_simple.append(toks[i+1])
    i = i + 1
        
# finish up by performing the + /
toks = toks_simple
ops = ops_simple
final_result = float(toks[0])
i = 0
for op in ops:
    if op == '+':
        final_result = final_result + float(toks[i+1])
    if op == '-':
        final_result = final_result - float(toks[i+1])
    i = i + 1

print(f'{str} has result {final_result}')
