from random import randint
print("Hello! Welcome to Random Guess Game :)")
print("Game Rules:")
print("-----------")
print("1. Select a Number from 0 - 9.")
print("2. Computer will automatically generates a Random Number.")
print("3. Untill The both numbers are not equal The game will be ON.")
print("4. if both numbers from Step 1 and Step 2 are equal The game will Ends.")
print("SHALL WE START: (Type YES/NO)")
sel=input()
if str(sel) == "yes" or str(sel)=="YES" or str(sel)=="Yes":
    for i in range(1,100):
        value = randint(0, 9)
        x=int(input("Now Enter any number 0 - 9:"))
        print("Computer generated number is "+str(value)+".")
        if value == x:
            y=i*10
            print ("Hey....U played well, The game is over and your score is:"+str(y)+".")
            break
        else:
            print("you played safely.")
elif str(sel) == "no" or str(sel)=="NO" or str(sel)=="No":
    print("Okay...play some other time :)")
            


