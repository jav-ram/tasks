# extract tree

# permutation lib
from itertools import product

# get permutations of choices

tree = []

size = 100
secuencia = []

txtTree = open("piramide.txt", "r")

for lines in txtTree:
    lines = lines.rstrip()  
    characters = lines.split(" ")
    tree.append(characters)



ongoing = True

lastIteration = []
ids = []

where = 0


for j in range(size-1, -1, -1):
    # search for the biggest one 
    id = 0

    if (j == size - 1):
        for i in range(0, size):
            if (tree[j][i] > tree[j][id]):
                #print tree[j][id]
                id = i
    else:
        
        if (ids[-1] == 0):
            if (j == 0):
                id = 0
            elif (tree[j][ids[-1]] < tree[j][ids[-1] + 1]):
                id = ids[-1]
            else:
                id = ids[-1] + 1
        elif (ids[-1] == len(tree[j])):
            if (tree[j][ids[-1] - 1] > tree[j][ids[-1] - 2]):
                id = ids[-1] - 1
            else:
                id = ids[-1] - 2

        else:
            print str(j) + "" +  str(ids[-1])
            
            if (tree[j][ids[-1]] > tree[j][ids[-1] - 1]):
                id = ids[-1]
            else:
                id = ids[-1] - 1

    print ids
    
    ids.append(int(id))


    
print("Path de atras para adelante (ids o posicion)" + str(ids))
resultado = 0
index = 0

p = size
for y in range(0, size):
    print tree[size - 1 -y][ids[y]]
    resultado = resultado + int(tree[size - 1 -y][ids[y]])

print("Base es de:" + str(resultado))
