import binascii
from implementations.assembler import Assembler

def main():
    cmd = input()
    if(cmd == 'a'):
        code_file = 'fibonacci.asm'
        program_assembler = Assembler()
        program_assembler.assemble(code_file)
        program_assembler.writeInOutputFile('b.bin')

        #outFile = open('fibonacci.bin', "wb")
        #outFile.write(_binaryProgram.binaryCode())


if __name__ == '__main__':
    main()
