
toys = [5, 3, 1, 4, 2]

for i in range(len(toys)):
    print(f"Iteration {i + 1}: {toys}")
    # Bubble sort algorithm
    # Compare adjacent/close elements and swap if they are in the wrong order.
    for j in range(len(toys) - 1):
        print(toys, "\n\nSwapping", toys[j], "and", toys[j + 1])
        # Compare adjacent elements and swap if they are in the wrong order
        if toys[j] > toys[j + 1]:
            # Swap the elements
            toys[j], toys[j + 1] = toys[j + 1], toys[j]

print(toys)