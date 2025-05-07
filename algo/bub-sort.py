# main branch
toys = [5, 3, 1, 4, 2]

for i in range(len(toys)):
    print(f"Iteration {i + 1}: {toys}")
    # Bubble sort algorithm
    # Compare adjacent/close elements and swap if they are in the wrong order.
    for j in range(len(toys) - 1):
        if toys[j] > toys[j + 1]:
            toys[j], toys[j + 1] = toys[j + 1], toys[j]

print(toys)