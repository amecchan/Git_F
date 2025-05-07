
toys = [5, 3, 1, 4, 2]

for i in range(len(toys)):
    print(f"\nIteration {i + 1}: {toys}")
    # Bubble sort algorithm
    # Compare adjacent/close elements and swap if they are in the wrong order.
    for j in range(len(toys) - 1):
        print(toys, "\nComparing", toys[j], "and", toys[j + 1])
        # Compare the current element with the next one
        if toys[j] > toys[j + 1]:
            # Swap if they are in the wrong order
            print("Swapping", toys[j], "and", toys[j + 1])
            toys[j], toys[j + 1] = toys[j + 1], toys[j]
        else:
            print("No swap needed")
    # Print the list after each iteration

print(toys)