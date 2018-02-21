import random
tixaianum=[]
for i in range(30):
    num=random.randint(-30,30)
    tixaianum.append(num)
print(tixaianum)
countingtriades = 0
for i in range(30):
    for j in range(i+1,30):
        for k in range(j+1,30):
            if tixaianum[i]+tixaianum[j]+tixaianum[k]==0:
                print('If you add the following 3 numbers, you get sum=0:',tixaianum[i], tixaianum[j], tixaianum[k] )

                countingtriades+=1


if countingtriades==0 :
    print('There is no team of 3 numbers that give you sum= 0 when you add them')
                      


