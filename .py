#bubble sort
data = [20, 8, 12, 16, 4, 2, 10, 22, 26, 18, 14, 6]
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Sorted array is:", data)
