import sys
dead = []
list1 = []

##function for detecting dead_ends
def detect_dead_end(place, list1) :
  verify = 0
  total = 0
  for i in list1 :
    if place in i :
      total += 1
  for i in list1 :
    if place in i:
      place_index = i.index(place)
      if total == 1 and i not in dead:
        if place_index == 0 :
          dead.append(i)
        elif place_index == 1 :
          set = i[0]
          maxx = 0
          for i in list1 :
            if set in i:
              maxx += 1  
          if maxx < 3:
            dead.append([i[1], i[0]])        
      elif i not in dead:
        verify = traverse(place, place, i, list1)
        if verify and place_index == 0 :
           dead.append(i) 
        elif verify and place_index == 1 :
          dead.append([i[1], i[0]]) 
          
##function for traversing
def traverse(fix, place, l1, list1) :
  if l1.index(place) == 0 :
    other_place = l1[1]
  else :
    other_place = l1[0] 
  for i in list1 :
    if other_place in i and i != l1 :
      other_place_index = i.index(other_place)
      if other_place_index == 0 :
        key = i[1]
      else :
        key = i[0]
      if key == fix :
         return False
      else :
       check1 = traverse(fix, other_place,  i, list1)   
       if check1 == 0 :
         return False
       else:
         return True     
  return True  
  
#function to filter dead ends
def filter_unwanted(place, dead) :
  total = 0
  for i in dead:
    if place in i:
      total += 1
  for i in dead:
    if place in i :
      if i.index(place) == 1 :
        remove_unwanted(place, total, dead)

#Function for removing dead ends
def remove_unwanted(place, total, dead) :
  for i in range(1, total) :
    for i in dead :
      if place in i :
        if i.index(place) == 0 :
          dead.remove(i)


# Function for taking imput through command line
def input_command_line():
	location1 = int(sys.argv[1])
	streets = int(sys.argv[2])
	j = 3
	for i in range((len(sys.argv) // 2) - 1):
		if j == len(sys.argv):
			break
		else:
			list1.append([int(sys.argv[j]) , int(sys.argv[j + 1])])
			j += 2
	for location in range(1,location1 + 1):
		detect_dead_end(location,list1)
		filter_unwanted(location,dead)
	print(len(dead))
	for i in dead:
		print(i[0] , end = " ")
		print(i[1])

input_command_line()
