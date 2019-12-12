import re
import copy
import math
FILE = 'input.txt'
pat = '\=(.*)\, '

inputData= [re.findall("[-\d]+", line) for line in open(FILE)]
inputData = [[int(n) for n in line] for line in inputData]


X=[line[0] for line in inputData]
Y=[line[1] for line in inputData]
Z=[line[2] for line in inputData]


initX=copy.deepcopy(X)
initY=copy.deepcopy(Y)
initZ=copy.deepcopy(Z)

def updateVelocity(coords,velocity):
        for x in range(len(coords)):
            vel=0
            for y in range(len(coords)):
                if coords[x]>coords[y]:
                    vel-=1
                if coords[x]<coords[y]:
                    vel+=1
            velocity[x]+=vel
        return velocity[:]

def updatePosition(coords,velocity):
    
    for x in range(len(coords)):
        coords[x]+=velocity[x]
    
    return coords[:]


def calculateEnergy(coords,velocity):
    Ep=[sum([abs(x) for x in line]) for line in list(map(list, zip(*coords)))]
    #print([sum([abs(x) for x in line]) for line in list(map(list, zip(*coords)))]) 
    Ek=[sum([abs(x) for x in line]) for line in list(map(list, zip(*velocity)))]
    Et=sum([x * y for x, y in zip(Ep, Ek)])

    return Et
   
def checkPosition(coords,velocity,initialValue):
        isZero =0
        if (coords==initialValue) and (velocity==[0,0,0,0]):
            isZero =1
        
        return isZero



def runSimulation(dirCoords,nsteps):

    coords=None
    velocity=None
    for i in range(nsteps):
        velocity=updateVelocity(coords if coords else dirCoords,velocity if velocity else [0,0,0,0])
        coords = updatePosition(coords if coords else dirCoords,velocity if velocity else [0,0,0,0])
        
    
    return coords[:], velocity[:]



def computeCycle(dirCoords,initCoords):
    steps=0
    isZero = 0
    coords=None
    velocity=None
    while not isZero:
        velocity=updateVelocity(coords if coords else dirCoords,velocity if velocity else [0,0,0,0])
        coords = updatePosition(coords if coords else dirCoords,velocity if velocity else [0,0,0,0])
        isZero = checkPosition(coords,velocity,initCoords)
        if isZero:
            print(f'Steps: {steps}\n\tcoords:\t{coords}\n\tvel:\t{velocity}')
            
            print('---------------------------------')

            return steps+1
            break

        steps += 1

def lcm(a,b):
    def gcd(c,d):
        while d:
            t = d; 
            d = c%d 
            c = t; 
        return c

    return int(a/gcd(a,b)*b)    

nsteps=1000
xx,vxx=runSimulation(X[:],nsteps)
yy,vyy=runSimulation(Y[:],nsteps)
zz,vzz=runSimulation(Z[:],nsteps)

Et=calculateEnergy([xx,yy,zz],[vxx,vyy,vzz])
print('================ PART 1 ==============')
print(f'Total energy after {nsteps} steps: {Et}')

print('================ PART 2 ==============')
print
stepsX=computeCycle(X,initX)
stepsY=computeCycle(Y,initY)
stepsZ=computeCycle(Z,initZ)
print(f'Total number of steps to initial state: {lcm(stepsY,lcm(stepsX,stepsZ))}\n')
