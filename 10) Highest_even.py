def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  print(max(evens))
highest_even([10,1,2,3,4,8])
