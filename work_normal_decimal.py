import os

def get_opcode(mnemonic):
    opcodes = {
        "ADD": "0000",
        "SUB": "0001",
        "AND": "0010",
        "OR": "0011",
        "SR": "0100",
        "SL": "0101",
        "SLT": "0110",
        "EQ": "0111",
        "SB": "1000",
        "LB": "1001",
        "LI": "1010",
        "LUI": "1011",
        "JMP": "1100",
        "BRA": "1101",
        "JR": "1110",
        "SPC": "1111",
        "MUL": "0000",
        "DIV": "0001",
        "REM": "0010",
        "XOR": "0011",
        "RR": "0100",
        "RL": "0101",
        "SGT": "0110",
        "NEQ": "0111",
        "MOV": "1000",
        "BBR/RST": "1110",
        "CLS": "1111"
    }
    return opcodes[mnemonic]

def get_binary_value(instruction):
    parts = instruction.split()
    opcode = get_opcode(parts[0])
    dest = bin(int(parts[1][1:]))[2:].zfill(4)
    src1 = bin(int(parts[2][1:]))[2:].zfill(4)
    src2 = "0000"
    if len(parts) == 4:
        src2 = bin(int(parts[3][1:]))[2:].zfill(4)
    binary_value = opcode + dest + src1 + src2
    hex_value = hex(int(binary_value, 2))[2:].zfill(4)
    decimal_value = int(hex_value, 16)
    return binary_value, hex_value, decimal_value

data = os.path.join(os.path.dirname(__file__), "pantufla.txt")
with open(data, "r") as f:
    instructions = f.readlines()
    print(instructions)

for instruction in instructions:
    binary_value, hex_value, decimal_value = get_binary_value(instruction.strip())
    print(instruction.strip(), "equals to", decimal_value)