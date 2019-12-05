import csv

with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]

programInstructions = [int(instr) for instr in programInstructions]


class IntcodeComputer:
    def __init__(self, instructions):
        self.instructions = instructions

    def run(self):
        processedInstr2 = self.instructions[:]  # duplicate input
        i = 0                               # set pointer
        for instr in processedInstr2:       # cycle through instructions
            opCode = processedInstr2[i]     # read opcode

            if opCode == 99:    # 99 = end of program
                break
            if opCode == 3:     # 3 = input value and save to a position given by parameter
                processedInstr2[processedInstr2[i+1]
                                ] = int(input('Input parameter:'))
                i += 2
            if opCode == 4:     # 4 = output value by parameter POSITION MODE
                print(f'Output value {processedInstr2[processedInstr2[i+1]]}')
                i += 2
            if opCode == 104:   # 4 = output value by parameter IMEDIATE MODE
                print(f'Output value {processedInstr2[i+1]}')
                i += 2
            if opCode == 1:  # 1 = sum of two parameters POSITION MODE
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] + \
                    processedInstr2[processedInstr2[i+2]]
                i += 4
            if opCode == 2:  # 2 = multiplication of two parameters POSITION MODE
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] * \
                    processedInstr2[processedInstr2[i+2]]
                i += 4
            if opCode == 1002:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]] * processedInstr2[i+2]
                i += 4
            if opCode == 1102:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] * processedInstr2[i+2]
                i += 4
            if opCode == 1101:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] + processedInstr2[i+2]
                i += 4
            if opCode == 1001:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]] + processedInstr2[i+2]
                i += 4
            if opCode == 101:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] + processedInstr2[processedInstr2[i+2]]
                i += 4
            if opCode == 102:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] * processedInstr2[processedInstr2[i+2]]
                i += 4
            if opCode == 5:
                if processedInstr2[processedInstr2[i+1]] > 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3
            if opCode == 105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3
            if opCode == 1005:
                if processedInstr2[processedInstr2[i+1]] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
            if opCode == 1105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
            if opCode == 6:
                if processedInstr2[processedInstr2[i+1]] == 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3
            if opCode == 106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[processedInstr2[i+2]]
                else:
                    i += 3
            if opCode == 1006:
                if processedInstr2[processedInstr2[i+1]] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
            if opCode == 1106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
            if opCode == 7:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 1007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 1107:
                if processedInstr2[i+1] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 8:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 1008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
            if opCode == 1108:
                if processedInstr2[i+1] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4

        return processedInstr2


computer = IntcodeComputer(programInstructions)
computer.run()
