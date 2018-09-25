#append
fruits=['apple','orange','kiwi']
frt = ['chikku','grapes','pomogranate']

fruits.append('banana')

print(fruits)

#extend
fruits.extend(frt)

print(fruits)

#insert
frt.insert(2,'banana')

print(frt)

#remove
frt.remove('banana')

print(frt)

#pop
frt.pop()

print(frt)


frt = ['chikku','grapes','pomogranate','apple','orange']

frt.pop(2)

print(frt)

frt.pop(-1)

print(frt)

#clear
frt.clear()

print(frt)

frt = ['chikku','grapes','pomogranate','apple','orange']

frt.index('apple')

#sort
frt.sort()

print(frt)

#reverse
frt.reverse()

print(frt)

frt 

#Copy
fruits = []
frt = []

fruits = ['apple','orange','kiwi']
frt = fruits.copy()

print(frt)
print(fruits)

print(id(frt))
print(id(fruits))

fruit+=['a']

print(frt)
print(fruits)

print(id(frt))
print(id(fruits))

#Dup
fruits = []
frt = []

fruits = ['apple','orange','kiwi']
frt = fruits


print(id(frt))
print(id(fruits))
