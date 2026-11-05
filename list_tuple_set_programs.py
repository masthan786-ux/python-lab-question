# 1. Find the smallest number in a list
numbers = [10, 5, 20, 3, 15]
print("Smallest number:", min(numbers))


# 2. Find the average of numbers in a list
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print("Average:", average)


# 3. Count how many times a number occurs
numbers = [1, 2, 3, 2, 4, 2, 5]
n = 2
print("Occurrences:", numbers.count(n))


# 4. Reverse a list
numbers = [1, 2, 3, 4, 5]
print("Reversed list:", numbers[::-1])


# 5. Sort a list in ascending order
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print("Sorted list:", numbers)


# 6. Find common elements of two tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
common = tuple(set(t1) & set(t2))
print("Common elements:", common)


# 7. Convert a list into a tuple
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)


# 8. Convert a tuple into a list
my_tuple = (10, 20, 30, 40)
my_list = list(my_tuple)
print("List:", my_list)


# 9. Find union, intersection and difference of two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)


# 10. Remove duplicate values using a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print("Without duplicates:", unique)
