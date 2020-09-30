# A tuple is a collection which is ordered and unchangeable. Allows duplicate numbers

#create tuple

fruits = ('Apples', 'Oranges', 'BlueBerries')

#single value needs trailing comma

fruits2 = ('Apples',)

#Cannot assign values to tuples

# fruits[1] = 'Pears' #won't work

#A set is a collection which is unordered and unindexed. No duplicate members.

#create set

fruits_set = {'Apples', 'Oranges', 'Pears'}

#check if in set

print('Apples' in fruits_set)