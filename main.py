def linearSearchAdvanced(array, search_value):
    for counter in range(len(array)):
        if array[counter] == search_value:
            return counter
    return -1

names = ["Bob", "John", "Max"]
print(linearSearchAdvanced(names, "Max"))
numbers = [123, 456, 789]
print(linearSearchAdvanced(numbers, 456))
print(linearSearchAdvanced([True, True, False], False))