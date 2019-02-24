import SimpleITK as sitk
import sqlite3
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


class BILDVERARBEITUNG():#كلاس معالجة الصور الطبية
    def bildanzeigen():#لإظهار صورة طبية من قاعدة البيانات
        d =''
        while True:
             x=int(input("Geben Sie die nummer oder die Nachname der Patient ,wer seinem medizieniche Bilder anzeigen möchten,1 nach nummer oder 2 nach Nachname,die andere Auswahlen beenden die Prosses "))#ادخل رقم او اسم المريض الذي تريد اظهار الصورة الطبية التابعة له ...1 بناءا على الرقم و2 بناءا على الكنية والخيارات الاخرى تنهي العملية
             if x==1 :#بناءا على الرقم
                 num=input("Geben Sie die nummer der Patient bitte ein")#الرجاء ادخال رقم المريض المطلوب
                 command="""select BILDER.SPEICHERORT from BILDER where BILDER.PatID={}""".format(num)
                 d=cur1.execute(command)

             elif x==2 :#بناءا على الاسم
                 name=input("Geben Sie die Nachname der Patient bitte ein")#الرجاء ادخال اسم المريض المطلوب
                 command="""select BILDER.SPEICHERORT from Patient left join BILDER on BILDER.PatID = Patient.PatID And Patient.NACHNAME='{}' """.format(name)
                 d = cur1.execute(command)

             else:#في حال تم ادخال رقم اخر يقوم بايقاف البرنامج
                 print("falsches Auswahl")
                 break

             d = d.fetchone()
             if d !=None:
                 d = d[0]
                 image = sitk.ReadImage(r"{}".format(d))
                 ar = sitk.GetArrayFromImage(image)[0, :, :]
                 plt.imshow(ar, cmap='gray')
                 plt.show()
    def bildhistugram():#لحساب هيستوغرام الصورة واظهاره
        d = ''
        while True:
            x = int(input(
                "Geben Sie die nummer oder die Nachname der Patient ,wer seinem medizieniche Bilder anzeigen möchten,1 nach nummer oder 2 nach Nachname,die andere Auswahlen beenden die Prosses "))  # ادخل رقم او اسم المريض الذي تريد اظهار الصورة الطبية التابعة له ...1 بناءا على الرقم و2 بناءا على الكنية والخيارات الاخرى تنهي العملية
            if x == 1:  # بناءا على الرقم
                num = input("Geben Sie die nummer der Patient bitte ein")  # الرجاء ادخال رقم المريض المطلوب
                command = """select BILDER.SPEICHERORT from BILDER where BILDER.PatID={}""".format(num)
                d = cur1.execute(command)

            elif x == 2:  # بناءا على الاسم
                name = input("Geben Sie die Nachname der Patient bitte ein")  # الرجاء ادخال اسم المريض المطلوب
                command = """select BILDER.SPEICHERORT from Patient left join BILDER on BILDER.PatID = Patient.PatID And Patient.NACHNAME='{}' """.format(
                    name)
                d = cur1.execute(command)

            else:  # في حال تم ادخال رقم اخر يقوم بايقاف البرنامج
                print("falsches Auswahl")
                break

            d=d.fetchone()
            if d!=None:
                d=d[0]
                image = sitk.ReadImage(r"{}".format(d))
                im=sitk.GetArrayFromImage(image)[0,:,:]
                plt.subplot(1,2,1)
                plt.imshow(im,cmap="gray")

                plt.subplot(1,2,2)
                plt.hist(im.flatten(),bins=50)
                plt.show()
    def bildfaltung():#لطوي الصورة باستخدام فلاتر مختلفة
        d = ''
        while True:
            x = int(input(
                "Geben Sie die nummer oder die Nachname der Patient ,wer seinem medizieniche Bilder anzeigen möchten,1 nach nummer oder 2 nach Nachname,die andere Auswahlen beenden die Prosses "))  # ادخل رقم او اسم المريض الذي تريد اظهار الصورة الطبية التابعة له ...1 بناءا على الرقم و2 بناءا على الكنية والخيارات الاخرى تنهي العملية
            if x == 1:  # بناءا على الرقم
                num = input("Geben Sie die nummer der Patient bitte ein")  # الرجاء ادخال رقم المريض المطلوب
                command = """select BILDER.SPEICHERORT from BILDER where BILDER.PatID={}""".format(num)
                d = cur1.execute(command)

            elif x == 2:  # بناءا على الاسم
                name = input("Geben Sie die Nachname der Patient bitte ein")  # الرجاء ادخال اسم المريض المطلوب
                command = """select BILDER.SPEICHERORT from Patient left join BILDER on BILDER.PatID = Patient.PatID And Patient.NACHNAME='{}' """.format(
                    name)
                d = cur1.execute(command)

            else:  # في حال تم ادخال رقم اخر يقوم بايقاف البرنامج
                print("falsches Auswahl")
                break

            d = d.fetchone()
            d=d[0]
            image=sitk.ReadImage(r'{}'.format(d))
            im=sitk.GetArrayFromImage(image)[0,:,:]
            while True:
                x=int(input("Wählen Sie die gewünchte Verarbeitung aus...1 für Mittelfilter ,2 für Binomiaöfilter,3 für detektion vertikaler Kanten ,4 für detektion horizontaler Kanten"))#اختر المعالجة المرغوبة ....1 لفلتر التوسيط , 2 لفلتر القطبية ,3 لكشف الحواف العمودية ,لكشف الحواف الافقية
                    kernel=1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])
                    gefiltert=signal.convolve(im,kernel)
                    plt.subplot(1,2,1)
                    plt.title("Das originale Bild")#الصورة الاصلية
                    plt.imshow(im,cmap='gray')
                    plt.subplot(1,2,2)
                    plt.title("Das gefilterte Bild (Fahltung mit Mittelfilter)")#الصورة المفلترة وبالطوي باستخدام فلتر التوسيط
                    plt.imshow(gefiltert,cmap='gray')
                    plt.show()
                elif x==2:
                    binfilter=1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
                    gefiltert=signal.convolve(im,binfilter)
                    plt.subplot(1, 2, 1)
                    plt.title("Das originale Bild")#الصورة الاصلية
                    plt.imshow(im, cmap='gray')
                    plt.subplot(1, 2, 2)
                    plt.title("Das gefilterte Bild (Fahltung mit Binomiaöfilter)")#الصورة المفلترة وبالطوي باستخدام فلتر التوسيط
                    plt.imshow(gefiltert, cmap='gray')
                    plt.show()
                elif x==3:
                    kernel=1/8*np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
                    gefiltert=signal.convolve(im,kernel)
                    plt.subplot(1, 2, 1)
                    plt.title("das originale Bild ")#الصورة الاصلية
                    plt.imshow(im, cmap='gray')
                    plt.subplot(1, 2, 2)
                    plt.title("Das gefilterte Bild (detektion vertikaler Kanten)")#الصورة المفلترة وبالطوي باستخدام كشف الحواف العمودية
                    plt.imshow(gefiltert, cmap='gray')
                    plt.show()
                elif x==4:
                    kernel=1/8*np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
                    gefiltert=signal.convolve(im,kernel)
                    plt.subplot(1, 2, 1)
                    plt.title("Das originale Bild")#الصورة الاصلية
                    plt.imshow(im, cmap='gray')
                    plt.subplot(1, 2, 2)
                    plt.title("Das gefilterte Bild (detektion horizontaler Kanten)")#الصورة المفلترة وبالطوي باستخدام كشف الحواف الافقية
                    plt.imshow(gefiltert, cmap='gray')
                    plt.show()
                else :
                    print("Die Prosses wurde beendet")#العملية انهيت
                    break
    def punktoperationen():#لإنجاز العمليات على العناصر النقطية (البكسل)
        d = ''
        while True:
            x = int(input("Geben Sie die nummer oder die Nachname der Patient ,wer seinem medizieniche Bilder anzeigen möchten,1 nach nummer oder 2 nach Nachname,die andere Auswahlen beenden die Prosses "))  # ادخل رقم او اسم المريض الذي تريد اظهار الصورة الطبية التابعة له ...1 بناءا على الرقم و2 بناءا على الكنية والخيارات الاخرى تنهي العملية
            if x == 1:  # بناءا على الرقم
                num = input("Geben Sie die nummer der Patient bitte ein")  # الرجاء ادخال رقم المريض المطلوب
                command = """select BILDER.SPEICHERORT from BILDER where BILDER.PatID={}""".format(num)
                d = cur1.execute(command)

            elif x == 2:  # بناءا على الاسم
                name = input("Geben Sie die Nachname der Patient bitte ein")  # الرجاء ادخال اسم المريض المطلوب
                command = """select BILDER.SPEICHERORT from Patient left join BILDER on BILDER.PatID = Patient.PatID And Patient.NACHNAME='{}' """.format(name)
                d = cur1.execute(command)

            else:  # في حال تم ادخال رقم اخر يقوم بايقاف البرنامج
                print("falsches Auswahl")
                break

            d = d.fetchone()
            if d != None:
                d = d[0]
                image = sitk.ReadImage(r"{}".format(d))
                im = sitk.GetArrayFromImage(image)[0, :, :]
                while True:
                    x=int(input("Welche Punktoperation möchten Sie implementieren...1 für Inversion ,2 für Binarisieren, 3 für Gamma-korrectur....die andere Auswahlen beenden die Prozess"))#اي عملية نقطية تريد تنفيذها ...1 للعكس ...2 للقطبية ...3 لتصحيح غاما ..والخيارت الاخرى توقف العملية
                    if x==1:
                        maxwert=np.max(im)
                        print(maxwert)
                        neu=maxwert-im
                        plt.subplot(1,2,1)
                        plt.title("Das originale Bild")#الصورة الاصلية
                        plt.imshow(im,cmap='gray')
                        plt.subplot(1,2,2)
                        plt.title("Das geänderte Bild ,nach Inversion")#الصورة المفلترة بعد العكس
                        plt.imshow(neu,cmap='gray')
                        plt.show()
                    elif x==2:
                        schranke=int(input("Geben Sie bitte die Schranke,die Sie mit binarisiern benutzen möchten "))#الرجاء ادخال الحد الذي سيتم التعديل وفقه
                        neu=(im>=schranke)*np.max(im)
                        plt.subplot(1, 2, 1)
                        plt.title("Das originale Bild")#الصورة الاصلية
                        plt.imshow(im, cmap='gray')
                        plt.subplot(1, 2, 2)
                        schranke=str(schranke)
                        plt.title("Das geänderte Bild,Binarisieren mit der Schrenke="+schranke)#الصورة المعدلة بالقطبية مع قيمة الحد = SCHRANK
                        plt.imshow(neu, cmap='gray')
                        plt.show()
                    elif x==3:
                        gamma=float(input("Geben Sie Gamma wert bitte ein,mit der Sie die Korrectur implementieren möchten"))#التي تريد ان يتم تصحيح غاما باستخدامها
                        neu = np.max(im)*(im/ np.max(im))**(1/gamma)
                        plt.subplot(1, 2, 1)
                        plt.title("Das originale Bild")#الصورة الاصلية
                        plt.imshow(im, cmap='gray')
                        plt.subplot(1, 2, 2)
                        gamma=str(gamma)
                        plt.title("Das geänderte Bild,Gamma Korrektur (Gamma= "+gamma+")")#الصورة المعدلة بتصحيح غاما
                        plt.imshow(neu, cmap='gray')
                        plt.show()
                    else:
                        print("Die Prosses wurde beendet")#العملية تم انهاؤها
                        break
BILDVERARBEITUNG.punktoperationen()