from math import ceil
import csv
from IntcodeComputer import IntcodeComputer
import matplotlib.pyplot as plt
import copy

with open('input.txt') as csv_file:
    programInstructions = list(csv.reader(csv_file, delimiter=','))[0]

programInstructions = [int(instr) for instr in programInstructions]


initialSize = [100,110]

hull = [[0]*initialSize[1] for i in range(initialSize[0])]

#print(hull)

startPosition = [ceil(initialSize[0]/2),ceil(initialSize[1]/2)]

#print(startPostion)


class Robot():
    def __init__(self, startPoint,startColor,hullData,instructions):
        
        self.start = startPoint
        self.startColor =startColor
        self.hull = copy.deepcopy(hullData)
        self.instructions= instructions
        
        self.painted={}

    def nextDir(self,currDir, rot):
        if currDir=='UP':
            if rot==0:
                nextD='LEFT' 
            else: nextD='RIGHT'     
        if currDir=='DOWN':
            if rot==0:
                nextD='RIGHT' 
            else: nextD='LEFT' 

        if currDir=='LEFT':
            if rot==0:
                nextD='DOWN' 
            else: nextD='UP' 

        if currDir=='RIGHT':
            if rot==0:
                nextD='UP' 
            else: nextD='DOWN'

        return nextD 

    def nextPos(self,currPos,currDir, rot):
        nextD=self.nextDir(currDir, rot)
        if nextD=='UP':
            nexP=[currPos[0]-1, currPos[1]]
        if nextD=='DOWN':
            nexP=[currPos[0]+1, currPos[1]]
        if nextD=='LEFT':
            nexP=[currPos[0], currPos[1]-1]
        if nextD=='RIGHT':
            nexP=[currPos[0], currPos[1]+1] 

        return nextD,nexP           

    def paint(self):
        opCode = None
        base=None
        nOut = 1
        currDir='UP'
        currPos=[self.start[0], self.start[1]]
        self.hull[currPos[0]][currPos[1]]=self.startColor
        pointer = None
        processedInstr = None
        while opCode != 99:
            
            computer = IntcodeComputer(processedInstr if processedInstr else
                                    self.instructions, [self.hull[currPos[0]][currPos[1]]], pointer if pointer else 0,base if base else 0)
            if not nOut % 2:
                pointer, outputDirection, processedInstr, opCode,base = computer.run('loop')
                
                nextD,nextP=self.nextPos(currPos,currDir, outputDirection)
                nOut += 1
                currPos=nextP
                currDir=nextD
            
            else:
                pointer, outputColor, processedInstr, opCode,base = computer.run('loop')
                
                if outputColor==0:
                    self.hull[currPos[0]][currPos[1]]=0
                if outputColor==1:
                    self.hull[currPos[0]][currPos[1]]=1 
                nOut += 1

                self.painted.setdefault(str(currPos[0])+str(currPos[1]),1 )
                
        return self.painted, self.hull

robot1=Robot(startPosition,0,hull,programInstructions)
robot1.paint()
print(sum(list(robot1.painted.values())))
plt.imshow(robot1.hull, cmap='Reds')


robot2=Robot(startPosition,1,hull,programInstructions)
robot2.paint()

plt.imshow(robot2.hull, cmap='binary_r',alpha=.8)

plt.axis('equal')
plt.axis('off')
plt.show()