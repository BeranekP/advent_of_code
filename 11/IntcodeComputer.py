class IntcodeComputer:
    def __init__(self, instructions, inputValues, pointer=0,base=0):
        self.instructions = instructions
        if isinstance(inputValues, list):
            if len(inputValues) > 1:
                self.inputValue1 = inputValues[0]
                self.inputValue2 = inputValues[1]
            if len(inputValues) == 1:
                self.inputValue1 = inputValues[0]

        self.pointer = pointer
        self.output = []
        self.base =base

    def run(self, mode=None):
        processedInstr2 = self.instructions[:]  # duplicate input
        i = self.pointer
        opCode = None
        hasRun = 0
        base = self.base
        
            
        while opCode != 99:
            
            idx=processedInstr2[i] + base
            if idx>len(processedInstr2):
                addMemory=[0]*((idx+1)-len(processedInstr2))
                processedInstr2.extend(addMemory)
                if mode == 'verbose':
                    print(f'Adding memory')

            opCode = processedInstr2[i]     # read opcode

            if mode == 'verbose':
                print(f'Pointer {i} -- Base {base} -- opCode {opCode}')

            if opCode == 3:     # 3 = input value and save to a position given by parameter

                if hasRun == 0:

                    processedInstr2[processedInstr2[i+1]] = self.inputValue1
                    i += 2
                    hasRun += 1
                    if mode == 'verbose':
                        print(f'{i} -- {base} -- input: {self.inputValue1} -->index {processedInstr2[i+1]}')
                    continue
                if hasRun > 0:

                    processedInstr2[processedInstr2[i+1]] = self.inputValue2

                    i += 2
                    hasRun += 1
                    continue
            if opCode == 203:     # 203 = input value and save to a position given by parameter

                

                if hasRun == 0:
                    
                    processedInstr2[processedInstr2[i+1] + base] = self.inputValue1
                    
                    
                    if mode == 'verbose':
                        print(f'{i} -- {base} -- input: {self.inputValue1} -->index {processedInstr2[i+1],base}={processedInstr2[i+1]+base}')
                    
                    hasRun += 1
                    i += 2
                    continue
                if hasRun > 0:

                    processedInstr2[processedInstr2[i+1] + base] = self.inputValue2

                    i += 2
                    hasRun += 1
                    continue
            if opCode == 4:     # 4 = output value by parameter POSITION MODE

                self.output = processedInstr2[processedInstr2[i+1]]
                i += 2  
                if mode == 'loop':
                    return i, self.output, processedInstr2, opCode,base

                if mode == 'verbose':
                    print(f'{i-2} -- {base} -- output: {self.output}')
                
                continue

            if opCode == 104:   # 104 = output value by parameter IMEDIATE MODE

                self.output = processedInstr2[i+1]
                i += 2
                if mode == 'loop':
                    return i, self.output, processedInstr2, opCode,base

                if mode == 'verbose':
                    print(f'{i-2} -- {base} -- output: {self.output}')

                

                continue

            if opCode == 204:   # 204 = output value by parameter RELATIV MODE

                self.output = processedInstr2[processedInstr2[i+1]+base]
                i += 2
                if mode == 'loop':
                    return i, self.output, processedInstr2, opCode,base

                if mode == 'verbose':
                    print(f'{i-2} -- output: {self.output}')

                
                continue

            if opCode == 1:  # 1 = sum of two parameters POSITION MODE
                
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] + \
                    processedInstr2[processedInstr2[i+2]]
                   
                i += 4
                
                continue
            
            if opCode == 101:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode == 201:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1] +
                                                                        base] + processedInstr2[processedInstr2[i+2]]
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
            if opCode == 2001:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue

            if opCode == 1201:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]+base] + processedInstr2[i+2]
                i += 4
                continue
            if opCode == 2201:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]+base] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode == 2101:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue

            if opCode ==10001:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==10101:
                processedInstr2[i+3]=  processedInstr2[i+1] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==11001:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==11101:
                processedInstr2[i+3]=  processedInstr2[i+1] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==11201:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]+base] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==12101:
                processedInstr2[i+3]= processedInstr2[i+1] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==12201:
                processedInstr2[i+3]= processedInstr2[processedInstr2[i+1]+base] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==20001:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[processedInstr2[i+1]] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==20101:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[i+1] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==21001:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[processedInstr2[i+1]] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==21101:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[i+1] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==20201:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] + processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==22001:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==21201:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] + processedInstr2[i+2]
                i += 4
                continue
            if opCode ==22101:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[i+1] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==22201:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] + processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue


            
            if opCode == 2:  # 2 = multiplication of two parameters POSITION MODE
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1]] * \
                    processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode == 102:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[i +
                                                                        1] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode == 202:
                processedInstr2[processedInstr2[i+3]] = processedInstr2[processedInstr2[i+1] +
                                                                        base] * processedInstr2[processedInstr2[i+2]]
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
            if opCode == 1202:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]+base] * processedInstr2[i+2]
                i += 4
                continue
            if opCode == 2202:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[processedInstr2[i+1]+base] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode == 2102:
                processedInstr2[processedInstr2[i+3]
                                ] = processedInstr2[i+1] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue

            if opCode ==10002:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==10102:
                processedInstr2[i+3]=  processedInstr2[i+1] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==11002:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==11102:
                processedInstr2[i+3]=  processedInstr2[i+1] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==11202:
                processedInstr2[i+3]=  processedInstr2[processedInstr2[i+1]+base] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==12102:
                processedInstr2[i+3]= processedInstr2[i+1] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==12202:
                processedInstr2[i+3]= processedInstr2[processedInstr2[i+1]+base] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==20002:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[processedInstr2[i+1]] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==20102:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[i+1] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==21002:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[processedInstr2[i+1]] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==21102:
                processedInstr2[processedInstr2[i+3]+base]=  processedInstr2[i+1] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==20202:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] * processedInstr2[processedInstr2[i+2]]
                i += 4
                continue
            if opCode ==22002:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==21202:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] * processedInstr2[i+2]
                i += 4
                continue
            if opCode ==22102:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[i+1] * processedInstr2[processedInstr2[i+2]+base]
                i += 4
                continue
            if opCode ==22202:
                processedInstr2[processedInstr2[i+3]+base]=   processedInstr2[processedInstr2[i+1]+base] * processedInstr2[processedInstr2[i+2]+base]
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
            if opCode == 205:
                if processedInstr2[processedInstr2[i+1]+base] > 0:
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
            if opCode == 2005:
                if processedInstr2[processedInstr2[i+1]] > 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
                else:
                    i += 3

                continue

            if opCode == 1105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3

                continue
            if opCode == 1205:
                if processedInstr2[processedInstr2[i+1]+base] > 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3

                continue
            if opCode == 2105:
                if processedInstr2[i+1] > 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
                else:
                    i += 3

                continue

            if opCode == 2205:
                if processedInstr2[processedInstr2[i+1]+base] > 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
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
            if opCode == 206:
                if processedInstr2[processedInstr2[i+1]+base] == 0:
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
            if opCode == 2006:
                if processedInstr2[processedInstr2[i+1]] == 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
                else:
                    i += 3
                continue
            if opCode == 1106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
                continue
            if opCode == 1206:
                if processedInstr2[processedInstr2[i+1]+base] == 0:
                    i = processedInstr2[i+2]
                else:
                    i += 3
                continue
            if opCode == 2106:
                if processedInstr2[i+1] == 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
                else:
                    i += 3
                continue
            if opCode == 2206:
                if processedInstr2[processedInstr2[i+1]+base] == 0:
                    i = processedInstr2[processedInstr2[i+2]+base]
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
            if opCode == 207:
                if processedInstr2[processedInstr2[i+1]+base] < processedInstr2[processedInstr2[i+2]]:
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
            if opCode == 2007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[processedInstr2[i+2]+base]:
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
            if opCode == 1207:
                if processedInstr2[processedInstr2[i+1]+base] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 2107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 2207:
                if processedInstr2[processedInstr2[i+1]+base] < processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            
            if opCode == 10007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue

            if opCode == 10107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 11007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue 
            if opCode == 11107:
                if processedInstr2[i+1] < processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 10207:
                if processedInstr2[processedInstr2[i+1]+base]< processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12007:
                if processedInstr2[processedInstr2[i+1]]< processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12107:
                if processedInstr2[i+1]< processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 11207:
                if processedInstr2[processedInstr2[i+1]+base]< processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12207:
                if processedInstr2[processedInstr2[i+1]+base]< processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 20007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 20107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue  
            if opCode == 21007:
                if processedInstr2[processedInstr2[i+1]] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 21107:
                if processedInstr2[i+1] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 21207:
                if processedInstr2[processedInstr2[i+1]+base] < processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue       
            if opCode == 22107:
                if processedInstr2[i+1] < processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 22207:
                if processedInstr2[processedInstr2[i+1]+base] < processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
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
            if opCode == 208:
                if processedInstr2[processedInstr2[i+1]+base] == processedInstr2[processedInstr2[i+2]]:
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
            if opCode == 2008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[processedInstr2[i+2]+base]:
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
            if opCode == 2108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 1208:
                if processedInstr2[processedInstr2[i+1]+base] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue
            if opCode == 2208:
                if processedInstr2[processedInstr2[i+1]+base] == processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]] = 1
                else:
                    processedInstr2[processedInstr2[i+3]] = 0
                i += 4
                continue

            if opCode == 10008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue

            if opCode == 10108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 11008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue 
            if opCode == 11108:
                if processedInstr2[i+1] == processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 10208:
                if processedInstr2[processedInstr2[i+1]+base]== processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12008:
                if processedInstr2[processedInstr2[i+1]]== processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12108:
                if processedInstr2[i+1]== processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 11208:
                if processedInstr2[processedInstr2[i+1]+base]== processedInstr2[i+2]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 12208:
                if processedInstr2[processedInstr2[i+1]+base]== processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[i+3] = 1
                else:
                    processedInstr2[i+3] = 0
                i += 4
                continue
            if opCode == 20008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 20108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue  
            if opCode == 21008:
                if processedInstr2[processedInstr2[i+1]] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 21108:
                if processedInstr2[i+1] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 21208:
                if processedInstr2[processedInstr2[i+1]+base] == processedInstr2[i+2]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue       
            if opCode == 22108:
                if processedInstr2[i+1] == processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue
            if opCode == 22208:
                if processedInstr2[processedInstr2[i+1]+base] == processedInstr2[processedInstr2[i+2]+base]:
                    processedInstr2[processedInstr2[i+3]+base] = 1
                else:
                    processedInstr2[processedInstr2[i+3]+base] = 0
                i += 4
                continue            


            if opCode == 9:    # 99 = end of program
                base += processedInstr2[processedInstr2[i+1]]
                i += 2
                continue
            if opCode == 109:    # 99 = end of program
                base += processedInstr2[i+1]
                i += 2
                continue
            if opCode == 209:    # 99 = end of program
                base += processedInstr2[processedInstr2[i+1]+base]
                i += 2
                continue
            if opCode == 99:    # 99 = end of program
                return i, self.output, processedInstr2, opCode,base
                break
