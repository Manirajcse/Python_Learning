some_list = ['a', 'b', 'c', 'b', 'd', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)




some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []
for char in range(len(some_list)):
    for i in range(char + 1,len(some_list)):
        if some_list[i] == some_list[char] and some_list not in duplicate_list:
            duplicate_list.append(some_list[char])
print(duplicate_list)




lista=['a','b','c','b','d','m','n','n']
dummy = []
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if(lista[i]==lista[j]):
            dummy.append(lista[i])
print(dummy)




letter_list_1 = ['a','b','c','b','d','m','n','n']
letter_list_2 = []
duplicate_found= []
for i in letter_list_1:
    if i not in letter_list_2:
        letter_list_2.append(i)
    else:
        duplicate_found.append(i)
print(duplicate_found)




some_list = ['a','b','c','b','d','m','n','n']
tmp = []
dups = []
for item in some_list:
    if item in tmp:
        dups.append(item)
    else:
        tmp.append(item)
print(dups)