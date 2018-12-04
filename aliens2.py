#Added variables and fixed grammar and punctuation

week = str("week")
lCheck = False
wCheck = False


print ("You will first input the number of aliens that landed of Earth")
print ("then input how many week have the aliens been on Earth for.")
print ("Please input the number of aliens that have landed on Earth.")

l = int(input())
if l > 0:
    print ("Please input how many weeks the aliens have been on Earth for.")            
 
    w = int(input())
    if w > 0:
        #calculations
        for i in range(w):
            if ( i == 1):
                week = "weeks"
            print("After", i + 1, week,", there are", l* 2**(i+1), "aliens on Earth.")
    else:
        print ("You didn't enter a valid answer.")
        
else:
    print ("You didn't enter a valid answer.")
