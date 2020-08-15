#Lists
'''
denoted by []
ordered 
mutable
indexed
support multiple data types
allows duplicates
more memory consumption than array

operations on Lists:
1.Add
2.update
3.delete
4.Access elements
5.slicing 
6.striding
7.concat
8.Iterable

'''
#adding to lists

#1.using append(adds at end)
'''
append adds at end of the list

'''
l=[1,2,3]
l.append(4)
print(l)

#2. add anywhere
#use insert
#insert(indexvalue,value)

l.insert(5,"a")
print(l)

#updating elements
#indexmethod

#list_name[index]=new_value

l[2]=7
print(l)

#deletion 

#1.using pop()
#removes last element by default 
l.pop()
print(l)

#2.using pop to remove any element

#pop(index)

l.pop(1)

print(l)

#using removing(char)

l.remove(1)
print(l)
