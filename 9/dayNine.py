import csv
from itertools import permutations

from IntcodeComputer import IntcodeComputer


# Prepare instructions
with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]

programInstructions = [int(instr) for instr in programInstructions]

# Run computer
inputValues = [1, 2]
for inputValue in inputValues:
    computer = IntcodeComputer(programInstructions, [inputValue])
    result = computer.run()
    print(f'Input: {inputValue} --->  Output: {result[1]}')
