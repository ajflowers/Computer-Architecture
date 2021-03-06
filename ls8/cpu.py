"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.ir = 0
        self.fl = 0

    def load(self):
        """Load a program into memory."""

        if len(sys.argv) != 2:
            print("usage: simple.py filename")
            sys.exit(1)

        filename = sys.argv[1]

        address = 0

        try:
            with open(filename) as f:
                for line in f:

                    # Ignore comments
                    comment_split = line.split("#")

                    # Strip out whitespace
                    num = comment_split[0].strip()

                    # Ignore blank lines
                    if num == '':
                        continue

                    val = int(num,2)
                    self.ram[address] = val
                    # print(num, val)
                    address += 1

        except FileNotFoundError:
            print("File not found")
            sys.exit(2)


        # # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, address):
        """read the value from the given address"""
        return self.ram[address]

    def ram_write(self, address, value):
        """update the given address with the new value provided"""
        self.ram[address] = value
        return

    def run(self):
        """Run the CPU."""
        
        running = True
        self.pc = 0

        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010

        while running:

            self.ir = self.ram_read(self.pc)

            if self.ir == HLT:
                """Halt the CPU (and exit the emulator)."""
                running = False

            elif self.ir == LDI:
                """
                LDI register immediate
                Set the value of a register to an integer.
                """
                self.reg[self.ram_read(self.pc + 1)] = self.ram_read(self.pc + 2)
                self.pc += 3

            elif self.ir == PRN:
                """
                PRN register` pseudo-instruction
                Print numeric value stored in the given register.
                """
                print(self.reg[self.ram_read(self.pc + 1)])
                self.pc += 2

            elif self.ir == MUL:
                self.alu('MUL', self.ram_read(self.pc + 1), self.ram_read(self.pc + 2))
                self.pc += 3

            else:
                # this should not activate unless PC has landed on invalid instruction
                self.trace()
                running = False
