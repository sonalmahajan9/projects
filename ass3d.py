def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Input
arr = list(map(int, input("Enter elements: ").split()))

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)

# Enter elements: 5 2 9 1 3
# Sorted array: [1, 2, 3, 5, 9]