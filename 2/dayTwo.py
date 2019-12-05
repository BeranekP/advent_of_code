import csv
import random
import math

with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]

programInstructions = [int(instr) for instr in programInstructions]

processedInstr = programInstructions[:]

def processInstructions(processedInstr):
    processedInstr2 = processedInstr[:]
    for i in range(len(processedInstr2)):
        opCode = processedInstr2[4*i]
        if opCode == 99:
            break
        num1 = processedInstr2[1+4*i]
        num2 = processedInstr2[2+4*i]
        resPos = processedInstr2[3+4*i]

        if opCode == 1:
            processedInstr2[resPos] = processedInstr2[num1] + \
                processedInstr2[num2]
        elif opCode == 2:
            processedInstr2[resPos] = processedInstr2[num1] * \
                processedInstr2[num2]
        elif opCode == 99:
            break

    return processedInstr2


while True:

    noun = math.floor(random.randint(0, len(processedInstr)-4))
    verb = math.floor(random.randint(0, len(processedInstr)-4))
    processedInstr[1] = noun
    processedInstr[2] = verb

    processedInstr1 = processInstructions(processedInstr)

    
    if processedInstr1[0] == 19690720:
        print(f'Noun = {noun}, Verb = {verb}')
        print(f'Result: {noun*100+verb}')
        break
