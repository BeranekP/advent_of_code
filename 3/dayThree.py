import matplotlib.pyplot as plt


# open input file a strip newline signs and commas
wires = [line.rstrip('\n') for line in open('input.txt')]
wires = [wire.split(",") for wire in wires]


def calcXY(wire):
    """ Calculates coords [X,Y] for each input direction and a number of steps """
    wireXY = [[0, 0]]
    steps = [0]
    for dirCoord in wire:
        direction = dirCoord[0]
        coord = int(dirCoord[1:])
        X = wireXY[-1][0]   # last X
        Y = wireXY[-1][1]   # last Y
        step0 = steps[-1]   # last step count

# check direction and compute coords with step 1
        if direction == 'R':
            for i in range(1, coord+1):
                wireXY.append([X+i, Y])
        elif direction == 'L':
            for i in range(1, coord+1):
                wireXY.append([X-i, Y])
        elif direction == 'U':
            for i in range(1, coord+1):
                wireXY.append([X, Y+i])
        elif direction == 'D':
            for i in range(1, coord+1):
                wireXY.append([X, Y-i])
        for i in range(1, coord+1):
            steps.append(step0+i)
    return (wireXY, steps)


wireXY_1, steps1 = calcXY(wires[0])
wireXY_2, steps2 = calcXY(wires[1])


def analyzeWires(wire1, steps1, wire2, steps2):

    # convert to tuples for sets
    iwire1 = [tuple(lst) for lst in wire1]
    iwire2 = [tuple(lst) for lst in wire2]

    # find intersections using set
    intersectionsCoords = set(iwire1).intersection(iwire2)

    # get indices for intersections except (0,0)
    indicesA = [iwire1.index(item)
                for item in intersectionsCoords if item != (0, 0)]
    indicesB = [iwire2.index(item)
                for item in intersectionsCoords if item != (0, 0)]

    # get coords for intersections from inputs
    intersections = [iwire1[i] for i in indicesA]

    # calculates Manhattan/Taxicab distance
    Manhattan = [(abs(item[0])+abs(item[1]))
                 for item in intersections]
    # get minimnal Manhattan
    minimalManhattan = min([item for item in Manhattan if item != 0])

    # find corresponding intersection
    minimalManhattanCoordsIdx = Manhattan.index(minimalManhattan)
    # using intersection because of abs in Manhattan
    minimalManhattanCoords = intersections[minimalManhattanCoordsIdx]

    # get steps for each curve
    stepsA = [steps1[i] for i in indicesA]
    stepsB = [steps2[i] for i in indicesB]

    # total number of steps for each intersection
    totalSteps = [stepsA[i] + stepsB[i] for i in range(len(stepsA))]

    # get coords of the intersection with minimal total steps
    indexTotal = totalSteps.index(min(totalSteps))
    intersectionsSteps = intersections[indexTotal]

    # visualize

    # wire 1

    plt.plot(*zip(*wireXY_1), color='steelblue')
    # wire 2

    plt.plot(*zip(*wireXY_2), color='tomato')

    # intersections
    plt.scatter(*zip(*intersections), color='black',
                s=10, zorder=10, label='intersections')

    # minimal Manhattan
    plt.scatter(
        minimalManhattanCoords[0], minimalManhattanCoords[1], color='lawngreen', marker="X", edgecolors='black', s=100, zorder=10, label='min. manhattan = ' + str(minimalManhattan))

    # minimal steps
    plt.scatter(
        intersectionsSteps[0], intersectionsSteps[1], color='goldenrod', marker="X", edgecolors='black', s=100, zorder=10, label='min. steps = ' + str(min(totalSteps)))

    plt.legend(loc='upper right')

    return intersections, minimalManhattan, min(totalSteps)


intersections, minimalManhattan, minTotalSteps = analyzeWires(
    wireXY_1, steps1, wireXY_2, steps2)
print(f'Minimal Manhattan: {minimalManhattan}\nMinimal steps: {minTotalSteps}')
plt.show()
