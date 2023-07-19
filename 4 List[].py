# List[], Tuples(), Set{}
# List = []
names = ['maniraj', 'Hari', 'Kathir', 'maniraj']
print(names)

#call particular value in list
print(names[0])

#slicing
print(names[0:2])

#negative slicing
print(names[-4:-2])
print(names[-4:-1])


# change or update the list
names[3] = 'subash'
print(names)

# methods - append
names.append('nivi')
print(names)


# methods - sort

#ascending
no = [9, 6, 3, 5, 1]
no.sort()
print(no)

#decending
no.sort(reverse=True)
print(no)

#add two List[]
addition = names + no
print(addition)

# length
print(len(names))
