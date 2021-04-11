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
                    self._binaryCode[self.end * 4: self.end * 4 + len(encoded_var)] = encoded_var
                    self.end = self.end * 4 + len(encoded_var)
                continue
            new_cmd, arg1, arg2, arg3 = line.replace('\n', '').split(' ')

        asm_file_text.close()
        asm_file_text = open(asm_file_name, encoding="utf-8")
        for i, line in enumerate(asm_file_text):
            new_cmd, arg1, arg2, arg3 = line.replace('\n', '').split(' ')

        asm_file_text.close()


    def writeInOutputFile(self, out_file_name):
        out_file = open(out_file_name, "wb") # "wb" write in binary mode
        out_file.write(self.binary_code)
        out_file.close()

    def fransformCmd(self, cmd_name, arg0, arg1, arg2):
        pass

'''UTF-32 (32-bit Unicode Transformation Format) is a fixed-length encoding used to 
encode Unicode code points that uses exactly 32 bits (four bytes) per code point '''
byteCode = bytearray(4)
		byteCode[0:1] = command.command.to_bytes(1, CommonByteOrder)
		byteCode[1:2] = command.localPtr.to_bytes(1, CommonByteOrder)
		byteCode[2:4] = command.farPtr.to_bytes(2, CommonByteOrder)
length = len(valueBytes)
		assert(length % 4 == 0)
		offset = self._cellsUsed * 4
		self._cellsUsed += length // 4
		self._binaryCode[offset: offset + length] = valueBytes