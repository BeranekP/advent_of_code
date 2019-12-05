
import itertools


LOW = 123257
HIGH = 647015
# calculate combinations of 6 digits in range 111111 and 999999
comb = list(itertools.combinations_with_replacement(
    [1, 2, 3, 4, 5, 6, 7, 8, 9], 6))


def concat(inputList):
    """ concatenates inputlist of lists into a list of numbers
    eg. [(1,1,1,1),(2,2,1,1)] -> [1111, 2211]
     """
    s = [str(i) for i in inputList]

    # Join list items using join()
    res = int("".join(s))

    return res


# Find combinations
concatComb_part1 = []
concatComb_part2 = []
for item in comb:

    duplications = []
    for i in item:
        duplications.append(item.count(i))

    if sum(duplications) > 6:  # check if password contains any duplication PART I
        newItem = concat(item)
        if (newItem > LOW) & (newItem < HIGH):
            concatComb_part1.append(newItem)
    if 2 in duplications:  # check if password contains a number twice PART II
        newItem = concat(item)
        if (newItem > LOW) & (newItem < HIGH):
            concatComb_part2.append(newItem)

print(f' Number of passwords Part 1: {len(concatComb_part1)}')
print(f' Number of passwords Part 2: {len(concatComb_part2)}')
