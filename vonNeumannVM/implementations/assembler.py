from commands import Commands


class Assembler:
    def __init__(self):
        cmds = Commands()
        self.list_of_commands = cmds.getCmds()
        self.binary_code = bytearray(1024)
        self.variables = {}
        self.end = 2 # 2 bytes for IP, SP reserved

    def assemble(self, asm_file_name):
        number_of_lines = 0
        asm_file_text = open(asm_file_name, encoding="utf-8")

        # find labels' line number
        for i, line in enumerate(asm_file_text):
            if 'vars:' in line:
                variables_names = line[5:].split(' ')
                for j in range(len(variables_names)):
                    {variables_names[j]: self.end}.update(self.variables)
                    encoded_var = variables_names[j].encode("cp1251")
                    self.binary_code[self.end * 4: self.end * 4 + len(encoded_var)] = encoded_var
                    self.end += len(encoded_var)//4
                continue
            new_cmd, arg0, arg1, arg2 = line.replace('\n', '').split(' ')
            if arg0 != 0:
                arg0 = variables_names[arg0]
            if arg1 != 0:
                arg1 = variables_names[arg1]
            if arg2 != 0:
                arg2 = variables_names[arg2]
            byteCode = bytearray(4)
            byteCode[0:1] = self.list_of_commands[new_cmd].to_bytes(1, 'big')
            byteCode[1:2] = variables_names.to_bytes(1, 'big')
            byteCode[2:3] = arg1.to_bytes(1, 'big')
            byteCode[3:4] = arg2.to_bytes(1, 'big')
            self.binary_code[self.end * 4: self.end * 4 + len(encoded_var)] = byteCode
            self.end += 1
        asm_file_text.close()


    def writeInOutputFile(self, out_file_name):
        out_file = open(out_file_name, "wb") # "wb" write in binary mode
        out_file.write(self.binary_code)
        out_file.close()

'''UTF-32 (32-bit Unicode Transformation Format) is a fixed-length encoding used to 
encode Unicode code points that uses exactly 32 bits (four bytes) per code point '''
