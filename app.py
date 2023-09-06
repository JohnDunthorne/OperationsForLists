numbers = [5, 4, 30, 45, 23, 44, 55, 100, 20, 55, 88]
# anything in [] square brackets separated by , comma becomes a list
numbers.append(500)
# this adds 500 to the end of the list
print(numbers)
for item in numbers:
    print(item)
# this just prints the numbers in a list
print(numbers[0])
# prints only the first item in list
print(numbers[0:])
# prints all numbers starting from first item in list
print(numbers[-3:])
# prints numbers starting 3rd from the end
print(numbers[3:6])
# prints numbers starting from the 4th to the 6th item
numbers.insert(0, 10)
# this adds a number to a specific index location
# in this case we added a 10 in the 0 position (the first number in the list)
numbers.insert(3, 333)
# here we added the number 333 in index 3 (our 4th number in the list)
print(numbers)
numbers.remove(55)
# this removes the 55 in the list
print(numbers)
numbers.clear()
# this clears all numbers from the list
print(numbers)
numbers = [2, 3, 4, 5, 6, 4, 7, 8, 9]
print(numbers)
numbers.pop()
# this removes the final entry in the list
print(numbers)
print(numbers.index(6))
# prints the index number for the first occurrence of this number in the list
print(numbers.count(4))
# this will show you how many times 4 appears in your list
numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers2.append(1000)
print(numbers)
print(numbers2)
# this is how to make a copy of your list, so you can start manipulating one
# but retain the original

# *********************************************
numbers_test = [1, 2, 3, 8, 4, 5, 6, 7, 5, 2, 8, 9]
numbers_test.sort()
print(numbers_test)
new_list = set(numbers_test)
print(new_list)
# this is a way to remove any duplicates from your list
# below is an alternative way to extract one of each item on a list
numbers_test2 = [1, 2, 3, 8, 4, 5, 6, 7, 5, 2, 8, 9]
uniques = []  # <this becomes a placeholder for 1 instance of each number
for number in numbers_test2:
    if number not in uniques:
        uniques.append(number)
print(uniques)
