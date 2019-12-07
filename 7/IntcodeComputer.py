class IntcodeComputer:
    def __init__(self, instructions, inputValues, pointer=0):
        self.instructions = instructions
        if isinstance(inputValues, list):
            if len(inputValues) > 1:
                self.inputValue1 = inputValues[0]
                self.inputValue2 = inputValues[1]
            if len(inputValues) == 1:
                self.inputValue1 = inputValues[0]

        self.pointer = pointer
        self.output = []

    def run(self, mode=None):
        processedInstr2 = self.instructions[:]  # duplicate input
        i = self.pointer
        opCode = None
        hasRun = 0
        while opCode != 99:

            opCode = processedInstr2[i]     # read opcode

            if opCode == 3:     # 3 = input value and save to a position given by parameter

                if hasRun == 0:

                    processedInstr2[processedInstr2[i+1]] = self.inputValue1
                    i += 2
                    hasRun += 1
                    continue
                if hasRun > 0:

                    processedInstr2[processedInstr2[i+1]] = self.inputValue2

                    i += 2
                    hasRun += 1
                    continue

            if opCode == 4:     # 4 = output value by parameter POSITION MODE

                self.output = processedInstr2[processedInstr2[i+1]]

                i += 2

                if mode == 'loop':
                    return i, self.output, processedInstr2, opCode

                continue

            if opCode == 104:   # 4 = output value by parameter IMEDIATE MODE

                self.output = processedInstr2[i+1]
                i += 2
                continue

            if opCode == 1:  # 1 = sum of two parameters POSITION MODE
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] + \
                    processedInstr2[processedInstr2[i+2]]
                i += 4
                continue

            if opCode == 2:  # 2 = multiplication of two parameters POSITION MODE
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] * \
                    processedInstr2[processedInstr2[i+2]]
                i += 4
                continue

            if opCode == 1002:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]] * processedInstr2[i+2]
                i += 4
                continue

            if opCode == 1102:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] * processedInstr2[i+2]
                i += 4
                continue

            if opCode == 1101:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] + processedInstr2[i+2]
                i += 4
                continue

            if opCode == 1001:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]] + processedInstr2[i+2]
                i += 4
                continue

            if opCode == 101:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue

            if opCode == 102:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode == 5:
                if processedInstr2[processedInstr2[i+1]] > 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3
                continue
            if opCode == 105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3

                continue

            if opCode == 1005:
                if processedInstr2[processedInstr2[i+1]] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3

                continue

            if opCode == 1105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3

                continue

            if opCode == 6:
                if processedInstr2[processedInstr2[i+1]] == 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3

                continue

            if opCode == 106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3

                continue

            if opCode == 1006:
                if processedInstr2[processedInstr2[i+1]] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
                continue
            if opCode == 1106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
                continue
            if opCode == 7:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 1007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 1107:
                if processedInstr2[i+1] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 8:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 1008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 1108:
                if processedInstr2[i+1] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 99:    # 99 = end of program
                return i, self.output, processedInstr2, opCode
                break
