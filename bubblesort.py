def option():
    return int(input("Option : ")) in range(1,2)

def main():
    list = []
    for count in range(10):
        list.append(int(input(f"{count}.enter the number :")))
    print(list)
    print("Choose one option:",
          "1. Bubble sort",
          "2. Show list again",
          sep='\n')
    if option() == 1:
        n = 0
        for n in range(0, (len(list) - 1), 1):
            i = 0
            for i in range(0, ((len(list) - 1) - n), 1):
                if list[i] <= list[i + 1]:
                    pass
                else:
                    x = list[i]
                    list[i] = list[i + 1]
                    list[ i + 1 ] = x
        print(list)
    else:
        print(list)

main()