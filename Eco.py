class Eco:
    def __init__(self):
        self.stack = []

    def run(self, code):
        self.code = code
        self.ip = 0
        self.stack = []
        try:
            while self.ip < len(code):
                data = code[self.ip].strip().split()
                if not data or data[0] == "#":
                    self.ip += 1
                    continue
                self.parse(data)
                self.ip += 1
        except Exception:
            pass

    def parse(self, cmd):
        if len(cmd) < 2:
            print(f'[ECO] Error!\n> Line {self.ip+1}, Operator doesn\'t exist.\n> \'{self.code[self.ip]}\'')
            raise Exception
        opcode = cmd[0]
        operand = cmd[1]
        if opcode == 'PUSH':
            try:
                self.stack.append(int(operand))
            except:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Expected integer.\n> \'{self.code[self.ip]}\'')
                raise Exception
        elif opcode == 'POP':
            if len(self.stack) == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            self.stack.pop()
        elif opcode == 'PRTCHR':
            if len(self.stack) == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            print(chr(self.stack[-1]), end='')
            self.stack.pop()
        elif opcode == 'PRTINT':
            if len(self.stack) == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            print(self.stack[-1], end='')
            self.stack.pop()
        elif opcode == 'DUP':
            if len(self.stack) == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            self.stack.append(self.stack[-1])
        elif opcode == 'INTIN':
            inp = input()
            if inp == '':
                self.stack.append(0)
            else:
                try:
                    self.stack.append(int(inp))
                except:
                    self.stack.append(0)
        elif opcode == 'CHRIN':
            inp = input()
            if inp == '':
                self.stack.append(0)
            else:
                try:
                    self.stack.append(ord(inp[0]))
                except:
                    self.stack.append(0)
        elif opcode == 'GOTO':
            try:
                if 0 <= int(operand) < len(self.code):
                    self.ip = int(operand)-1
                else:
                    print(f'[ECO] Error!\n> Line {self.ip+1}, Out of bounds.\n> \'{self.code[self.ip]}\'')
                    raise Exception
            except:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Expected integer.\n> \'{self.code[self.ip]}\'')
                raise Exception
        elif opcode == 'IF':
            if len(self.stack) == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            if self.stack[-1] == 0:
                self.ip += 1
        elif opcode == 'ADD':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = (self.stack[-1] + self.stack[-2])
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added)
        elif opcode == 'SUB':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = (self.stack[-2] - self.stack[-1])
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added)
        elif opcode == 'MUL':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = (self.stack[-1] * self.stack[-2])
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added)
        elif opcode == 'DIV':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            if self.stack[-1] == 0:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Zero Division.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = (self.stack[-2] // self.stack[-1])
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added)
        elif opcode == 'EQL':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = 1 if self.stack[-1] == self.stack[-2] else 0
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added)
        elif opcode == 'REV':
            if len(self.stack) <= 1:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added1 = self.stack[-1]
            added2 = self.stack[-2]
            self.stack.pop()
            self.stack.pop()
            self.stack.append(added1)
            self.stack.append(added2)
        elif opcode == 'FETCH':
            try:
                int(operand)
            except:
                print(f'[ECO] Error!\n> Line {self.ip+1}, Expected integer.\n> \'{self.code[self.ip]}\'')
                raise Exception
            if len(self.stack) < int(operand):
                print(f'[ECO] Error!\n> Line {self.ip+1}, Stackunderflow.\n> \'{self.code[self.ip]}\'')
                raise Exception
            added = self.stack[-int(operand)]
            self.stack.pop(-int(operand))
            self.stack.append(added)
        else:
            print(f'[ECO] Error!\n> Line {self.ip+1}, Unknown command.\n> \'{self.code[self.ip]}\'')
            raise Exception

code = []

eco = Eco() 
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        try:
            with open(file, 'r') as f:
                src = f.read().splitlines()
                eco.run(src)
        except Exception as e:
            print(f'[ECO] Error!\n> File not found.')
    else:
        print('''  ____
 | ___)
 | |     ___   ___
 | __)  / __) /   \\
 | |_   |(__  | O |
 |____) \\___) \\___/''')
        print('Eco repl, enter EXIT 0 to exit.')
        code = []
        while True:
            line = input('> ')
            data = line.strip().split()
            if len(data) <= 1:
                if not data:
                    continue
                elif data[0] == '#':
                    continue
                print(f'[ECO] Error!\n> Operand doesn\'t exist.\n> \'{line}\'')
                continue
            elif data[0] == 'EXIT':
                try:
                    int(data[1])
                    exit()
                except:
                    print(f'[ECO] Error!\n> Expected integer.\n> \'{line}\'')
                    continue
            elif data[0] == 'RUN':
                try:
                    int(data[1])
                    eco.run(code)
                    print()
                    continue
                except:
                    print(f'[ECO] Error!\n> Expected integer.\n> \'{line}\'')
                    continue
            elif data[0] == 'FULL':
                try:
                    int(data[1])
                    print('\n'.join(code))
                    continue
                except:
                    print(f'[ECO] Error!\n> Expected integer.\n> \'{line}\'')
                    continue
            code.append(line)
