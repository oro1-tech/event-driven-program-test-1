#insertion sort algorithm
data = [20, 8, 12, 16, 4, 2, 10, 22, 26, 18, 14, 6]
for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and key < data[j]:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
print("Sorted array is:", data)
