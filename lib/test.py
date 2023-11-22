# s = [4, 6, 3, 9, 3, 5, 10, 1, 3, 2]
# s.sort()
# print (s.count(7))
my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tvalue):
   return tvalue[1]
my_list.sort(key = sort_tuple)
print(my_list)

