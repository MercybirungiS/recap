# using range to create the same list
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# range start
nums = range(0, 12)
nums_list = list(nums)
print(nums_list)
# range stop
nums = range(12)
nums_list = list(nums)
print(nums_list)

even_nums = range(2, 11, 2)
even_nums_list = list(even_nums)
print(even_nums_list)
# enumerate()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
indexed_letters = enumerate(letters)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)

numbers = [1, 2, 3, 4, 5, 6]
indexed_numbers = enumerate(numbers, start=9)
indexed_numbers_list = list(indexed_numbers)
print(indexed_numbers_list)

# map()
nums = [2.4, 3.6, 4.8, 5.2, 6.2]
rnd_nums = map(round, nums)
rnd_nums_list = list(rnd_nums)
print(rnd_nums_list)

nums = [1, 2, 3, 4, 5]
sqrd_nums = map(lambda x: x**2, nums)
print(list(sqrd_nums))

#for loop
sqrd_nums =[]
for num in nums:
    sqrd_nums .append(num**2)
print(sqrd_nums)
# boolean indexing
a = [10, 12, 14, 16, 18, 20]
pos = []
for num in a:
    if num > 12:
       pos.append(num)
       print(pos)

months = ['January', 'July', 'March']
months.append('December')
print(months)
x = [1,2,3]
x.append(4) # append method can only add one element to the list
print(x)
x.extend([6, 7, 8, 9]) # extend method add multiple elements to a list
print(x)






