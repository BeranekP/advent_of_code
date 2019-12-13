
import csv
import sys
from IntcodeComputer import IntcodeComputer

with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]


programInstructions = [int(instr) for instr in programInstructions]

mode=2 # 2 = play mode
if mode==2:
    programInstructions[0]=2

opCode = None
base = None
pointer = None
processedInstr = None
countBlocks = 0
i = 0
nOut=1
score=0
joystick=None
ballX=0
paddleX=0
while opCode != 99:
    
    computer = IntcodeComputer(processedInstr if processedInstr else
                               programInstructions, [joystick if joystick else 0], pointer if pointer else 0, base if base else 0)
    if nOut==(1+i*3):
        pointer, outputX, processedInstr, opCode, base = computer.run('loop')    
        
    if nOut==(2+i*3):    
        pointer, outputY, processedInstr, opCode, base = computer.run('loop')
        
        
    if nOut==(3+i*3):
        pointer, outputID, processedInstr, opCode, base = computer.run('loop')
        
        
    
    
    if not nOut%3:

        i+=1
        if outputID==2:
            countBlocks += 1
        if outputID==3:
            paddleX, paddleY=outputX, outputY
            
        if outputID==4:
            ballX, ballY=outputX, outputY
               

        if outputX==-1 and outputY==0 and mode==2:
            score=outputID
            print(f'Score: {score}')
            

        if ballX>paddleX:
            joystick=1
        elif ballX<paddleX:
            joystick=-1
        else:joystick=0


    nOut+=1
        
if mode!=2:
    print(f'Number of block tiles: {countBlocks}')

    