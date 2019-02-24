class k:
    def __init__(self,l,m):
        self.__m=m
        self.__l=l

    def s(self):
        M=self.__m*self.__l
        return (M)


while True:
    try:
        x=int(input("1 fur messung nichs fur das program abbrechen"))
    except:
        print("das program wird abgebrochen")
        break

    if (x==1):
           l=int(input("das lenght bitte"))
           m=int(input("die masse"))
           BML=m/l**2
           if (BML<18.5):
                 print("untergewicht")
           else:
                 if (BML < 25):
                       print("in ordnung")
                 else:
                       print("übber")
    elif (x!=1):
        print("falsches auswahl")
