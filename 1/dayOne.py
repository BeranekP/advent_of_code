

lineList = [line.rstrip('\n') for line in open('input.txt')]
moduleMass = [int(line) for line in lineList]
fuel = [mass//3-2 for mass in moduleMass]

print(f'Fuel Part I: {sum(fuel)}')


##################


def calculateFuel(mass):
    curFuel = mass//3-2
    fuel = curFuel
    while curFuel//3-2 >= 0:
        curFuel = curFuel//3-2
        fuel += curFuel
    return fuel


fuel = [calculateFuel(mass) for mass in moduleMass]

print(f'Fuel Part II: {sum(fuel)}')
