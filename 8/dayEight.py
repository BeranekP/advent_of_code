from collections import Counter
import matplotlib.pyplot as plt

width = 25
height = 6
FILE = 'input.txt'
with open(FILE, 'r') as f:
    imageData = f.read().rstrip('\n')
    imageData = [int(char) for char in imageData]


chunks = [imageData[i:i + width*height]
          for i in range(0, len(imageData), width*height)]


counts = [Counter(chunk) for chunk in chunks]
nZeros = [count[0] for count in counts]
idx = nZeros.index(min(nZeros))
print(f'Part1: {counts[idx][2]*counts[idx][1]}')


chunks = [[chunk[i:i + width]
           for i in range(0, width*height, width)] for chunk in chunks]
image = [[None for i in range(0, width)] for i in range(0, height)]

layers = len(chunks)
layer = len(chunks[0])
value = len(chunks[0][0])

for l in range(value):
    for k in range(layer):
        for j in range(layers):
            if chunks[j][k][l] == 2:
                continue
            elif chunks[j][k][l] == 1:
                image[k][l] = 1
                break
            elif chunks[j][k][l] == 0:
                image[k][l] = 0
                break

                #print(f'Current value {k,l} is {image[k][l]}')

# print(image)
plt.imshow(image, cmap='binary')
plt.axis('equal')
plt.axis('off')
plt.show()
