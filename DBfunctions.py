import sqlite3

connection = sqlite3.connect(r"C:\\Users\\Waref Ali\\Desktop\\database3.db")
cur1 = connection.cursor()

class DBMain():
       def DBdatenanzeigen():#ﻲﻓ ﺓﺩﻮﺟﻮﻤﻟا ﺕﺎﻣﻮﻠﻌﻤﻟا ﻞﻛ ﺭﺎﻬﻇﻹ db
           command="""select Patient.PatID,Patient.VORNAME,Patient.NACHNAME,Patient.GEBURTSDATUM,Patient.LETZTENBESUCH,BILDER.untersuchungstyp,BILDER.Bildgebungdatum,BILDER.SPEICHERORT from Patient left join Bilder on Patient.PatID=Bilder.PatID """
           cur1.execute(command)
           infos=cur1.fetchall()
           print(infos)


       def neuPat(pid=0, x="S", y="Z", z="k", l="m"):#ﻝا ﻰﻟا ﺪﻳﺪﺟ ﺾﻳﺮﻣ ﺔﻓﺎﺿﺇdb
           pid = int(input("Bitte geben sie die PatientID ein"))#ﺾﻳﺮﻤﻟا ﻢﻗﺭ ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           x = input("Bitte geben Sie die Vorname des Patients ein")#ﺾﻳﺮﻤﻠﻟ ﻝﻭﻻا ﻢﺳﻻا ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           y = input("Bitte geben Sie die Nachname des Patients ein")#ﺾﻳﺮﻤﻠﻟ (ﺔﻴﻨﻜﻟا) ﻲﻧﺎﺜﻟا ﻢﺳﻻا ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           z = input("Bitte geben Sie das Geburtsdatum des Patients ein")#ﺾﻳﺮﻤﻟا ﺩﻼﻴﻣ ﺦﻳﺭﺎﺗ ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           l = input("Bitte geben Sie das Datum des letztenversuch ,wie hier(14 uhr 12.10.2018),ein") #ﻞﻜﺸﻟا ﻲﻓ ﺢﺿﻮﻣ ﻮﻫ ﺎﻤﻛ ﺓﺭﺎﻳﺯ ﺮﺧا ﺦﻳﺭﺎﺗ ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           neu=(pid,x,y,z,l)
           command1 = """INSERT INTO Patient VALUES(?,?,?,?,?)"""
           cur1.execute(command1,neu)
           connection.commit()
           command2="""select * from Patient"""
           cur1.execute(command2)
           infos=cur1.fetchall()
           print(infos)

       def löschen():#ﺾﻳﺮﻣ ﺕﺎﻧﺎﻴﺑ ﻑﺬﺤﻟ

           while True:
               x = int(input("Wählen Sie bitte aus..1 für löschen nach Name,2 löscheln nach nummer,3 die  gesamte Tabele leeren, die andere Auswahlen beenden die Prozess" ))#ﺾﻳﺮﻤﻟا ﻢﻗﺭ ﻖﻳﺮﻃ ﻦﻋ ﻑﺬﺤﻠﻟ 2ﻭ ﻢﺳﻻا ﻖﻳﺮﻃ ﻦﻋ ﻑﺬﺤﻠﻟ 1 ﻢﻗﺮﻟا ﺭﺎﻴﺘﺧا ءﺎﺟﺮﻟا

               if x==1:# ﻢﺳﻻا ﻰﻠﻋ اءﺎﻨﺑ ﻑﺬﺤﻟا
                   name=input("Geben Sie die Name des Patients,dessen Daten Sie aus DB löschen möchten")#ﻪﺗﺎﻧﺎﻴﺑ ﻑﺬﺣ ﺪﻳﺮﺗ ﻱﺬﻟا ﺾﻳﺮﻤﻟا ﻢﺳا ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
                   x="""select PatID from Patient where Patient.VORNAME='{}' """.format(name)
                   command1="""delete  from Patient where VORNAME='{}' """.format(name)
                   command2="""delete from BILDER where PatID=?"""
                   cur1.execute(command1)
                   cur1.execute(command2,x)
                   connection.commit()


               elif (x==2):#ﺾﻳﺮﻤﻟا ﻢﻗﺭ ﻰﻠﻋ اءﺎﻨﺑ ﻑﺬﺤﻟا
                   id=input("Geben Sie das ID des Patient,dessen Daten Sie aus DB löschen möchten")
                   command3="""delete  from Patient where PatID = {}""".format(id)
                   command4="""delete from BILDER where PatID={}""".format(id)
                   cur1.execute(command3)
                   cur1.execute(command4)
                   connection.commit()
               elif (x==3):
                   command5="""delete  from Patient """
                   command6="""delete from BILDER"""
                   cur1.execute(command5)
                   cur1.execute(command6)
                   connection.commit()
               else:#ﻊﺑﺎﺘﻟا ﻕﻼﻏاﻭ ﺕﺎﻧﺎﻴﺒﻟا ﺽﺮﻌﺑ ﻡﻮﻘﻳ ﺮﺧا ﻢﻗﺭ ﻝﺎﺧﺩا ﻢﺗ اﺫاﻭ
                   command7 = """select * from Patient left join Bilder on Patient.PatID=Bilder.PatID"""
                   cur1.execute(command7)
                   infos = cur1.fetchall()
                   print(infos)
                   print("Die prozess wurde beendet")

                   break
       def suche(x=1):#ﺕﺎﻧﺎﻴﺒﻟا ﺓﺪﻋﺎﻗ ﻲﻓ ﻦﻴﻌﻣ ﺾﻳﺮﻣ ﻦﻋ ﺚﺤﺒﻠﻟ

           while True:
               wahl=int(input("MÖCHTEN Sie nach ID oder nach Vorname des Patients suchen ,bitte drücken sie 1 für ID oder 2 für Vorname ,die andere Auswahlen beenden die Prozess" ))#ﺔﻴﻠﻤﻌﻟا ﻲﻬﻨﺗ ﻯﺮﺧﻻا ﺕاﺭﺎﻴﺨﻟاﻭ ﻢﺳﻷﻟ 2ﻭ ﻢﻗﺮﻟا ﻖﻳﺮﻃ ﻦﻋ ﺚﺤﺒﻠﻟ 1 ﻂﻐﺿا ءﺎﺟﺮﻟا  ﺾﻳﺮﻤﻠﻟ ﻝﻭﻻا ﻢﺳﻻا ﻡا ﻢﻗﺮﻟا ﻰﻠﻋ اءﺎﻨﺑ ﺚﺤﺒﻟا ﺪﻳﺮﺗا
               if (wahl ==1):#ﻢﻗﺮﻟا ﻖﻳﺮﻃ ﻦﻋ ﺚﺤﺒﻠﻟ
                   x=input("Geben Sie bitte die Nummer des angegraften Patients ein")#ﺏﻮﻠﻄﻤﻟا ﺾﻳﺮﻤﻟا ﻢﻗﺭ ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
                   command1="""select * from Patient where PatID is ?"""
                   cur1.execute(command1,x)
                   pat1=cur1.fetchall()
                   print(pat1)

               elif (wahl==2):#ﻢﺳﻻا ﻖﻳﺮﻃ ﻦﻋ ﺚﺤﺒﻠﻟ

                   x=input("Geben Sie bitte die Vorname des angegraften Patients ein")#ﺏﻮﻠﻄﻤﻟا ﺾﻳﺮﻤﻠﻟ ﻝﻭﻻا ﻢﺳﻻا ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
                   command2 = """select * from Patient where VORNAME =(?)"""

                   cur1.execute(command2,(x,))
                   pat2 = cur1.fetchall()
                   print(pat2)

               else:#ﺔﻴﻠﻤﻌﻟا ءﺎﻬﻧا ﻢﺘﻳ ﺮﺧا ﻢﻗﺭ ﻝﺎﺧﺩا ﻢﺗ ﻝﺎﺣ ﻲﻓ

                   print("Die Prozess wurde beendet")#ﺔﻴﻠﻤﻌﻟا ﺖﻴﻬﻧا
                   break
       def bilderhinfügen(PatID=0 ,bildtyp= "n", Datum= "n", speicherort= "n"):#ﺕﺎﻧﺎﻴﺒﻟا ﺓﺪﻋﺎﻗ ﻰﻟا ﺔﻴﺒﻃ ﺓﺭﻮﺻ ﺔﻓﺎﺿﻹ
           patid=input("Geben Sie bitte die Nummer der Patient ein")#ﺾﻳﺮﻤﻟا ﻢﻗﺭ ﻝﺎﺧﺩا ءﺎﺟﺮﻟا
           x=input("WAS IST DER ART DER UNTERSUCHUNG ,X-Ray,Ultraschall(Sonografie),Szintigrafie(GamaKamera),Endoskopie,Computertomografie,MRT oder Elektrokardiogramm EKG")#ﺔﻴﺒﻄﻟا ﺓﺭﻮﺼﻟا ﻉﻮﻧ ﺎﻣ .......
           y=input("Wann wurde die Bildgebung stattgefunden")#ﺮﻳﻮﺼﺘﻟا ﻢﺗ ﻰﺘﻣ
           z=input("Welsches Bild möchten Sie hinfügen")#ﺓﺭﻮﺼﻟا ﻥاﻮﻨﻋ ﻒﻴﻀﻨﻣ ﻥﻮﻫ) ﺎﻬﺘﻓﺎﺿا ﺪﻳﺮﺗ ﺓﺭﻮﺻ ﻱا)
           command1="""INSERT INTO BILDER VALUES(?,?,?,?)"""
           bilder1=(patid,x,y,z)
           cur1.execute(command1,bilder1)
           connection.commit()



DBMain.DBdatenanzeigen()
DBMain.neuPat()
DBMain.bilderhinfügen()
DBMain.löschen()
connection.close()

###DBMain.suche()
