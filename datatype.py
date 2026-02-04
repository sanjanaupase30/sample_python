#integer
a=10
b=2
print("Addition :", a+b)
print("substraction is :", a-b)
print("multiplication is :", a*b)
print("division is :", a/b)
print()

#float
m=2.4
n=3.5
print("addition is :", m+n)
print("round value is :",round(m))
print()

#String 
p="Sanjana"
print("Upper :",p.upper())
print("lower :",p.lower())
print("title :",p.title())
print("length : ",len(p))
print()
 #boolean
s=True
d=False
print("AND value is :",s and d)
print("OR value is :", s or d)
print("NOT value is :" , not s)
print()
#list 
f=[1,2,3,4,5]
f.append(23)
print("appended list" ,f)
f.insert(1,6)
print("inserted element :",f)
f.remove(2)
print("removed element is :",f)
f.sort()
print("sorted list :",f)
print()

#tuple 
g=(1,2,3,4,5,3)
print("index is :",g.index(5))
print("count is :",g.count(3))
print()

#set 
h={1,2,3,4,5}
h.add(6)
print("added element :",h)
h.remove(4)
print("removed element is :",h)
h.update([5,7])
print("updated elemnt is :",h)
print()