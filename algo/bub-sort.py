# main branch
toys = [5, 3, 1, 4, 2]

for i in range(len(toys)):
    for j in range(len(toys) - 1):
        if toys[j] > toys[j + 1]:
            toys[j], toys[j + 1] = toys[j + 1], toys[j]

print(toys)