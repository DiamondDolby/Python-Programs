def sortnsearch():
  list = []
  for count in range(5):
    list.append(int(input(f"{count}.enter int :")))
  print(list)
  print("Do you want to Sort or Search in your list?",
        "1. Sort list",
        "2.Search list",
        sep='\n')
  if (option() == 1):
    print("Bubble sort or Insertion sort?",
          "1. Bubble Sort",
          "2. Insertion Sort",
          sep='\n')
    if option() == 1:
      i = 0
      for i in range(0, (len(list) - 1), 1):
        j = 0
        for j in range(0, ((len(list) - 1) - i), 1):
            if list[j] <= list[j + 1]:
                pass
            else:
                x = list[j]
                list[j] = list[j + 1]
                list[j + 1] = x
      print(list)
    else:
      i = 0
      for i in range(0, (len(list) - 1), 1):
        j = i + 1
        x = list[j]
        list.remove(list[j])
        while j > 0:
            if x < list[j - 1]:
                if (j - 1) == 0:
                    list.insert(0, x)
                j = j - 1
            elif x == list[j - 1]:
                list.insert((j - 1), x)
                j = j - 1
            else:
                if x > list[j - 1]:
                    list.insert(j, x)
                break
      print(list)
  else:
    search = int(input("search value : "))
    print("1.linear search ")
    if option() == 1:
      i = 0
      for i in range(0, (len(list) - 1), 1):
        if search == list[i]:
            print("True, list index:", i)
        else:
            if i == (len(list) - 1):
                print("false")
            else:
                pass

def option():
  return int(input("1 or 2? :  ")) in range(1, 2)


sortnsearch()

#binary search is not included in this program