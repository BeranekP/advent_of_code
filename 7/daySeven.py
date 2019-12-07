import csv
from itertools import permutations

from IntcodeComputer import IntcodeComputer


# Prepare instructions
with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]

programInstructions = [int(instr) for instr in programInstructions]


numAplifiers = 5

###################### Part 1 ##########################
ampSettings = list(permutations(
    range(0, numAplifiers), numAplifiers))  # Part 1


outputs = []
for setting in ampSettings:
    output = None
    for value in setting:
        # print([value, output if output else 0])
        computer = IntcodeComputer(
            programInstructions, [value, output if output else 0])
        result = computer.run()
        output = result[1]

    outputs.append(output)

print('\n------------ PART 1 --------------')
print(f'Max output in series: {max(outputs)}')

###################### Part 2 ##########################
ampSettings2 = list(permutations(
    range(5, 5+numAplifiers), numAplifiers))

outputs = []

print('\n------------ PART 2 --------------')
nameComputers = ['A', 'B', 'C', 'D', 'E']
for setting in ampSettings2:
    output = {}
    pointer = {}
    processedInstr = {}
    computers = {}
    opCode = None
    nSetting = [0, 0, 0, 0, 0]

    while opCode != 99:
        for n in range(len(nameComputers)):

            if opCode != 99:

                if nSetting[n] == 0:
                    computers[nameComputers[n]] = IntcodeComputer(programInstructions, [setting[n],
                                                                                        0 if nameComputers[n] == 'A' else output[nameComputers[n-1]]])

                    nSetting[n] += 1

                else:
                    computers[nameComputers[n]] = IntcodeComputer(processedInstr[nameComputers[n]], [
                        output[nameComputers[n-1]]], pointer[nameComputers[n]])

                    nSetting[n] += 1

                pointer[nameComputers[n]], output[nameComputers[n]
                                                  ], processedInstr[nameComputers[n]], opCode = computers[nameComputers[n]].run('loop')

                if opCode == 99:
                    outputs.append(output['E'])
            else:
                break

print(f'Max output in loop: {max(outputs)}')
