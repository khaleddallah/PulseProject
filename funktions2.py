import sqlite3

#connection = sqlite3.connect(r"./database3.db")
#cur1 = connection.cursor()

class funktions:
       curl=0
       connection=0
       def ConnectToDB(path):
           funktions.connection = sqlite3.connect(path)
           funktions.cur1 = funktions.connection.cursor()

       def MaxIdPatientsTable():
           command="""SELECT Max(PatID) FROM Patient"""
           funktions.cur1.execute(command)
           infos=funktions.cur1.fetchall()
           return(infos[0][0])


       def DBdatenanzeigen():
           command="""select Patient.PatID,Patient.VORNAME,Patient.NACHNAME,Patient.GEBURTSDATUM,Patient.LETZTENBESUCH,BILDER.untersuchungstyp,BILDER.Bildgebungdatum,BILDER.SPEICHERORT from Patient left join Bilder on Patient.PatID=Bilder.PatID """
           funktions.cur1.execute(command)
           infos=funktions.cur1.fetchall()
           return(infos)

       def AllPatientDB():
           command="""select * from Patient """
           funktions.cur1.execute(command)
           infos=funktions.cur1.fetchall()
           return(infos)

       def neuPat(x):
           command1 = """INSERT INTO Patient VALUES(?,?,?,?,?)"""
           funktions.cur1.execute(command1,x)
           funktions.connection.commit()
           command2="""select * from Patient"""
           funktions.cur1.execute(command2)
           infos=funktions.cur1.fetchall()
           print(infos)

       def loschen(id):
           command3="""delete  from Patient where PatID = {}""".format(id)
           command4="""delete from BILDER where PatID={}""".format(id)
           funktions.cur1.execute(command3)
           funktions.cur1.execute(command4)
           funktions.connection.commit()

       def sucheID(x=-1):
           if (x== -1):
               print('Error ID')
               return(-1)
           command1="""select * from Patient where PatID=(?)"""
           s=str(x)
           funktions.cur1.execute(command1,s)
           pat1=funktions.cur1.fetchall()
           return(pat1)

       def sucheName(x,y):
           if (x=='' and y==''):
               print('Error Name')
               return('0')

           elif (y==''):
               print('x=',x)
               command2 = """select * from Patient where VORNAME =(?)"""
               funktions.cur1.execute(command2,(x,))
               pat2 = funktions.cur1.fetchall()
               return(pat2)

           else:
               print('x=',x)
               print('y=',y)
               command2 = """select * from Patient where VORNAME =(?) and NACHNAME =(?)"""
               funktions.cur1.execute(command2,(x,y))
               pat2 = funktions.cur1.fetchall()
               return(pat2)


       def bilderhinfügen(PatID=0 ,bildtyp= "n", Datum= "n", speicherort= "n"):
           patid=input("Geben Sie bitte die Nummer der Patient ein")
           x=input("WAS IST DER ART DER UNTERSUCHUNG ,X-Ray,Ultraschall(Sonografie),Szintigrafie(GamaKamera),Endoskopie,Computertomografie,MRT oder Elektrokardiogramm EKG")
           y=input("Wann wurde die Bildgebung stattgefunden")
           z=input("Welsches Bild möchten Sie hinfügen")
           command1="""INSERT INTO BILDER VALUES(?,?,?,?)"""
           bilder1=(patid,x,y,z)
           funktions.cur1.execute(command1,bilder1)
           funktions.connection.commit()



# funktions.DBdatenanzeigen()
# funktions.neuPat()
# funktions.bilderhinfügen()
# funktions.löschen()
# connection.close()

###funktions.suche()
