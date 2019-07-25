# this is a list
a = [3, 10, -1]
print(a)
# we can append/add item to a list
#append() is a predefined function for list data type
a.append(1)
print(a)
# we can add different types of data to a single list
a.append("hello")
print(a)
# we can add list inside a list
a.append([1, 3])
print(a)

#to delete a item
#lets delete the last item
a.pop()
#pop() is a predefined function for list data type
#pop() function is used to delete the last item in the list
print(a)
#lete delete string
a.pop()
print(a)

#to retrieve the item from the list
print(a[0])
print(a[3])

#change the content of the list
a[0] = 100
print(a)