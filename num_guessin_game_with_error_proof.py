import random


def print_banner():
    print("   ___     ___    _  _     ___     ___     ___    _____    ___                           ")
    print("  / __|   / _ \  | \| |   / __|   | _ \   /   \  |_   _|  / __|                          ")
    print(" | (__   | (_) | | .` |  | (_ |   |   /   | - |    | |    \__ \     _       _       _    ")
    print("  \___|   \___/  |_|\_|   \___|   |_|_\   |_|_|   _|_|_   |___/   _(_)_   _(_)_   _(_)_  ")
    print()
    print()
    print(" __   __   ___    _   _          __      __ ___    _  _               _                  ")
    print(" \ \ / /  / _ \  | | | |    o O O\ \    / // _ \  | \| |     o O O   | |                 ")
    print("  \ V /  | (_) | | |_| |   o      \ \/\/ /| (_) | | .` |    o        |_|                 ")
    print("  _|_|_   \___/   \___/   TS__[O]  \_/\_/  \___/  |_|\_|   TS__[O]  _(_)_                ")
    print()
    print()


# Main Code

a = int 
b = int

b = random.randrange(1,50,1)
a = b * 10




while ( a!=0):
    try:
        a = int(input("Enter your guess [Enter 0 to Quit]: "))
        if(a==0) :
            break
    except:
         print("Enter only number/integer")
         continue   
        

    if(a==b) :
        print("Congrats!! You got it Correct")
        print_banner()
        break
    else:
        if (a > b) :
            print("oops!! You guess is not Correct; Enter a smaller value")
        else:
            print("oops!! You guess is not Correct; Enter a bigger value")
    


print("Howz it!! Thanks for playing...!")




