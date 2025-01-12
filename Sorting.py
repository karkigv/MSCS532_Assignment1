def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print("Original array:", array)
    insertion_sort_descending(array)
    print("Sorted array in descending order:", array)