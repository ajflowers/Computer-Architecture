## ALU ops
ADD = 0b10100000
SUB = 0b10100001
MUL = 0b10100010
DIV = 0b10100011
MOD = 0b10100100

INC = 0b01100101
DEC = 0b01100110

CMP = 0b10100111

AND = 0b10101000
NOT = 0b01101001
OR  = 0b10101010
XOR = 0b10101011
SHL = 0b10101100
SHR = 0b10101101

alt_instructions = {
    ADD: 'ADD',
    SUB: 'SUB',
    MUL: 'MUL',
    DIV: 'DIV',
    MOD: 'MOD',
    INC: 'INC',
    DEC: 'DEC',
    CMP: 'CMP',
    AND: 'AND',
    NOT: 'NOT',
    OR: 'OR',
    XOR: 'XOR',
    SHL: 'SHL',
    SHR: 'SHR'
}

## PC mutators

CALL = 0b01010000
RET = 0b00010001

INT = 0b01010010
IRET = 0b00010011

JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110
JGT = 0b01010111
JLT = 0b01011000
JLE = 0b01011001
JGE = 0b01011010

## Other

NOP = 0b00000000

HLT = 0b00000001

LDI = 0b10000010

LD  = 0b10000011
ST  = 0b10000100

PUSH = 0b01000101
POP = 0b01000110

PRN = 0b01000111
PRA = 0b01001000


