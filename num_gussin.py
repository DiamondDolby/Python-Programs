import random
a = int 
b = int

b = random.randrange(1,50,1)
a = b * 10

while ( a!=0):

     a = int(input("Enter your guess [Enter 0 to Quit]: "))
     if(a==0):
        break
     if(a==b) :
        print("Congrats!! You got it Correct")
        break
     else:
        if (a > b) :
            print("oops!! You guess is not Correct; Enter a smaller value")
        else:
            print("oops!! You guess is not Correct; Enter a bigger value")