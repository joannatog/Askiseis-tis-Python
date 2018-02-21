import datetime
daysnum = 0

tags = { 0 : 'Deftera' ,1 : 'Triti' ,2 : 'Tetarti' ,3 : 'Pempti' ,4 : 'Paraskevi' ,5 : 'Savvato' ,6 : 'Kyriaki' }
simeramera = datetime.datetime.now().day		
simeraminas = datetime.datetime.now().month 
simeraetos = datetime.datetime.now().year



datetime.datetime.today()
datetime.datetime.today().weekday()
dayoftheweek =tags[datetime.datetime(simeraetos, simeraminas, simeramera).weekday()]	#H deftera  einai to 0, h triti to 1, tetarti to 2 kai paei legontas, h kyriaki einai to 6

for y in range(0,10):
            for m in range(simeraminas+1,12):
                        if dayoftheweek == tags[datetime.datetime(simeraetos,m,simeramera).weekday()] :
                                daysnum = daysnum + 1

            simeraminas = 1
            simeraetos += 1



print "For the next ten years, the ", dayoftheweek, "days with date", simeramera,  "of the month are :", daysnum
