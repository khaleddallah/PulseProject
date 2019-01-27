import sqlite3

connection = sqlite3.connect(r"./database3.db")
cur1 = connection.cursor()

class funktions():
       def DBdatenanzeigen():#لإظهار كل المعلومات الموجودة في db
           command="""select Patient.PatID,Patient.VORNAME,Patient.NACHNAME,Patient.GEBURTSDATUM,Patient.LETZTENBESUCH,BILDER.untersuchungstyp,BILDER.Bildgebungdatum,BILDER.SPEICHERORT from Patient left join Bilder on Patient.PatID=Bilder.PatID """
           cur1.execute(command)
           infos=cur1.fetchall()
           print(infos)


       def neuPat(pid=0, x="S", y="Z", z="k", l="m"):#إضافة مريض جديد الى الdb
           pid = int(input("Bitte geben sie die PatientID ein"))#الرجاء ادخال رقم المريض
           x = input("Bitte geben Sie die Vorname des Patients ein")#الرجاء ادخال الاسم الاول للمريض
           y = input("Bitte geben Sie die Nachname des Patients ein")#الرجاء ادخال الاسم الثاني (الكنية) للمريض
           z = input("Bitte geben Sie das Geburtsdatum des Patients ein")#الرجاء ادخال تاريخ ميلاد المريض
           l = input("Bitte geben Sie das Datum des letztenversuch ,wie hier(14 uhr 12.10.2018),ein") #الرجاء ادخال تاريخ اخر زيارة كما هو موضح في الشكل
           neu=(pid,x,y,z,l)
           command1 = """INSERT INTO Patient VALUES(?,?,?,?,?)"""
           cur1.execute(command1,neu)
           connection.commit()
           command2="""select * from Patient"""
           cur1.execute(command2)
           infos=cur1.fetchall()
           print(infos)

       def löschen():#لحذف بيانات مريض

           while True:
               x = int(input("Wählen Sie bitte aus..1 für löschen nach Name,2 löscheln nach nummer,3 die  gesamte Tabele leeren, die andere Auswahlen beenden die Prozess" ))#الرجاء اختيار الرقم 1 للحذف عن طريق الاسم و2 للحذف عن طريق رقم المريض

               if x==1:# الحذف بناءا على الاسم
                   name=input("Geben Sie die Name des Patients,dessen Daten Sie aus DB löschen möchten")#الرجاء ادخال اسم المريض الذي تريد حذف بياناته
                   x="""select PatID from Patient where Patient.VORNAME='{}' """.format(name)
                   command1="""delete  from Patient where VORNAME='{}' """.format(name)
                   command2="""delete from BILDER where PatID=?"""
                   cur1.execute(command1)
                   cur1.execute(command2,x)
                   connection.commit()


               elif (x==2):#الحذف بناءا على رقم المريض
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
               else:#واذا تم ادخال رقم اخر يقوم بعرض البيانات واغلاق التابع
                   command7 = """select * from Patient left join Bilder on Patient.PatID=Bilder.PatID"""
                   cur1.execute(command7)
                   infos = cur1.fetchall()
                   print(infos)
                   print("Die prozess wurde beendet")

                   break
       def suche(x=1):#للبحث عن مريض معين في قاعدة البيانات

           while True:
               wahl=int(input("MÖCHTEN Sie nach ID oder nach Vorname des Patients suchen ,bitte drücken sie 1 für ID oder 2 für Vorname ,die andere Auswahlen beenden die Prozess" ))#اتريد البحث بناءا على الرقم ام الاسم الاول للمريض  الرجاء اضغط 1 للبحث عن طريق الرقم و2 للأسم والخيارات الاخرى تنهي العملية
               if (wahl ==1):#للبحث عن طريق الرقم
                   x=input("Geben Sie bitte die Nummer des angegraften Patients ein")#الرجاء ادخال رقم المريض المطلوب
                   command1="""select * from Patient where PatID is ?"""
                   cur1.execute(command1,x)
                   pat1=cur1.fetchall()
                   print(pat1)

               elif (wahl==2):#للبحث عن طريق الاسم

                   x=input("Geben Sie bitte die Vorname des angegraften Patients ein")#الرجاء ادخال الاسم الاول للمريض المطلوب
                   command2 = """select * from Patient where VORNAME =(?)"""

                   cur1.execute(command2,(x,))
                   pat2 = cur1.fetchall()
                   print(pat2)

               else:#في حال تم ادخال رقم اخر يتم انهاء العملية

                   print("Die Prozess wurde beendet")#انهيت العملية
                   break
       def bilderhinfügen(PatID=0 ,bildtyp= "n", Datum= "n", speicherort= "n"):#لإضافة صورة طبية الى قاعدة البيانات
           patid=input("Geben Sie bitte die Nummer der Patient ein")#الرجاء ادخال رقم المريض
           x=input("WAS IST DER ART DER UNTERSUCHUNG ,X-Ray,Ultraschall(Sonografie),Szintigrafie(GamaKamera),Endoskopie,Computertomografie,MRT oder Elektrokardiogramm EKG")#ما نوع الصورة الطبية .......
           y=input("Wann wurde die Bildgebung stattgefunden")#متى تم التصوير
           z=input("Welsches Bild möchten Sie hinfügen")#اي صورة تريد اضافتها (هون منضيف عنوان الصورة)
           command1="""INSERT INTO BILDER VALUES(?,?,?,?)"""
           bilder1=(patid,x,y,z)
           cur1.execute(command1,bilder1)
           connection.commit()



funktions.DBdatenanzeigen()
funktions.neuPat()
funktions.bilderhinfügen()
funktions.löschen()
connection.close()

###funktions.suche()
