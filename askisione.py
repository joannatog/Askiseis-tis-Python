import random
mylist = []
for j in range(1000):
    for i in range(100):
        numblist=[]
        for num in range(5):
            x = random.randint(1,80)
            numblist.append(x)

        mylist.append(numblist)

  
    winning = []
    for winnumb in range(5):
        already = False 
        y = random.randint(1,80)
        if y in winning:
            already = True
        else:
            winning.append(y)
            already = False
     
        while already == True:
            y = random.randint(1,80)
            if y not in winning:
                already = False
                winning.append(y)

    for player in range (100):
        score=0
        for num in range(5):
                if numblist[num] == winning[num]:
                    score = score + 1


        if score == 5:
            print "You have won!"
        



