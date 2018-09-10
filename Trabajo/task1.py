tree = []
# read file
txtTree = open("piramide.txt", "r")
# make it an array
for lines in txtTree:
    lines = lines.rstrip()  
    characters = lines.split(" ")
    tree.append(characters)

for y in range((len(tree) - 2), -1, -1):
    for x in range(0, len(tree[y])):
        if int(tree[y + 1][x]) > int(tree[y + 1][x + 1]):
            tree[y][x] = int(tree[y][x]) + int(tree[y + 1][x])
        else:
            tree[y][x] = int(tree[y][x]) + int(tree[y + 1][x + 1])

print "La base de la piramide es de: " + str(tree[0][0])