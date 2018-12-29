import sys

reg = dict()
reg['a'] = 0
reg['b'] = 0

program = []
for l in sys.stdin.readlines():
    words = l.strip().split()
    program.append(words)

pc = 0
while True:
    print pc, reg
    if pc < 0 or pc >= len(program):
        break
    row = program[pc]
    instr = row[0]
    if instr == 'inc':
        param1 = row[1]
        reg[param1] += 1
        pc += 1
    if instr == 'tpl':
        param1 = row[1]
        reg[param1] *= 3
        pc += 1
    if instr == 'hlf':
        param1 = row[1]
        reg[param1] /= 2
        pc += 1
    if instr == 'jmp':
        param1 = int(row[1])
        pc += param1
    if instr == 'jie':
        param1 = row[1][:-1]
        param2 = int(row[2])
        if reg[param1] % 2 == 0:
            pc += param2
        else:
            pc += 1
    if instr == 'jio':
        param1 = row[1][:-1]
        param2 = int(row[2])
        if reg[param1] == 1:
            pc += param2
        else:
            pc += 1
print reg['b']
