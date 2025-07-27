# creating a tuple
a = (1,2,3,4,5,6,7,8,9,0)
print(a)
empty_tuple = ()
print(empty_tuple)
mixed_tuple=(1,'w','qwer',3.9098, 5)
print(mixed_tuple)
#modifing the tuple is not allowed
# adding elements to the tuple is not allowed
# removing elements from the tuple is not possible
# tuple functions
print(len(a)) # length of the tuple
print(max(a)) # Maximum value of the tupple
print(min(a)) # minimum value of thr tuple
print(sum(a)) # sum of he elements in the tuple
print(sorted(a)) # sorting the tuple
print(a.count(1)) # count of the occurance of the 1 in the given tuple
print(a.index(4)) # index of the first occurance of the eleemtnt in the tuple
#slicing the tuple
print(a[2:5]) # printing elements from index 2 to 4
print(a[:6]) # printing the elements from start to index 5
print(a[3:]) # printing the elements from index 3 to end
print(a[-1]) # printing the last elemennt in the tuple
print(a[-5]) # printing the element from the end of the 5th index
#tuple comprehension
b = list(a)
print(b.append(30))
print(b)
b[2] = 20 
print(b)
a = tuple(b)
print(a) # converting the list back to tuple