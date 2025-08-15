# Example file for Programming Foundations: Algorithms by Joe Marini
# Bubble sort algorithm


def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print("Starting state: ", list1)
bubbleSort(list1)
print("Final state: ", list1)
