#added comment
week = str("week")
# check for wrong input variable
lCheck = False
wCheck = False 

#intro
print ("You will first input the number of aliens that landed of Earth")
print ("then input how many week have the aliens been on Earth for.")
#loop for question one
while lCheck==False:
    try:
        l = int(input("Please input the number of aliens that have landed on Earth. "))
        # user input a aceaptable answer
        if l > 0:
            lCheck=True
        # user input a negative    
        else:
            print("That is not a positive integer.")
     # user input a letter or other type unaceaptable input           
    except ValueError:
        print("That is not a number.")

while wCheck==False:
    try:
        w = int(input("Please input in how many weeks the aliens have been on Earth for. "))
        # user inputed a aceaptable answer
        if w > 0:
            wCheck = True
        # user input a negative 
        else:
            print("That is not a positive integer.")
    # user input a letter or other type unaceaptable input
    except ValueError:
        print("This is not a number.")


#calculations
for i in range(w):
    if (i == 1):
        week = "weeks"
    print("After", i + 1, week,", there are", l* 2**(i+1), "aliens on Earth.")
