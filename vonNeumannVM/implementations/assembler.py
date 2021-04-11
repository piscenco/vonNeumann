class Assembler:
    def __init__(self):
        pass

    def assemble(self, asm_file_name):
        asm_file_text = open(asm_file_name, encoding="utf-8")
        for i, line in enumerate(asm_file_text):
            cmd, arg1, arg2, arg3 = line.replace('\n', '').split(' ')
            print(cmd, arg1, arg2)
