import SimpleITK as sitk
import sqlite3
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


class BILDVERARBEITUNG():#كلاس معالجة الصور الطبية

    def bildhistugram(d):#لحساب هيستوغرام الصورة واظهاره
        if (d!=None):
            image = sitk.ReadImage(r"{}".format(d))
            im=sitk.GetArrayFromImage(image)[0,:,:]
            fig=plt.figure()
            plt.imshow(im,cmap="gray",figure=fig)
            plt.hist(im.flatten(),bins=50,figure=fig)
            imgTemp="tmp.jpg"
            plt.savefig(imgTemp, bbox_inches='tight',transparent=True,figure=fig)
            return (imgTemp)
        else :
            print('!!! Error in Image Path')

    # def savee(x):
    #     # image = sitk.ReadImage(r"{}".format(x))
    #     # im= sitk.GetArrayFromImage(image)[:,:,0]
    #     # plt.imshow(im, cmap="gray")
    #     # plt.axis("off")
    #     # plt.show()
    #     plt.savefig('out.png', bbox_inches='tight',transparent=True, pad_inches=0,figure=x)


    def bildfaltung(d,x):#لطوي الصورة باستخدام فلاتر مختلفة
        if d != None:
            image=sitk.ReadImage(r'{}'.format(d))
            im=sitk.GetArrayFromImage(image)[:,:,0]
            #اختر المعالجة المرغوبة ....1 لفلتر التوسيط , 2 لفلتر القطبية ,3 لكشف الحواف العمودية ,لكشف الحواف الافقية
            if (x==1):
                kernel=1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])
                gefiltert=signal.convolve(im,kernel)
                plt.subplot(1,2,1)
                plt.title("Das originale Bild")#الصورة الاصلية
                plt.imshow(im,cmap='gray',figure=fig)
                plt.subplot(1,2,2)
                plt.title("Das gefilterte Bild (Fahltung mit Mittelfilter)")#الصورة المفلترة وبالطوي باستخدام فلتر التوسيط
                plt.imshow(gefiltert,cmap='gray')
                imgTemp="tmp.jpg"
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True,figure=fig)
                return (imgTemp)
            elif (x==2):
                binfilter=1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
                gefiltert=signal.convolve(im,binfilter)
                fig=plt.figure()
                # plt.title("Das gefilterte Bild (Fahltung mit Binomiaöfilter)")#الصورة المفلترة وبالطوي باستخدام فلتر التوسيط
                plt.axis("off")
                plt.imshow(gefiltert, cmap='gray',figure=fig)
                imgTemp="tmp.jpg"
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0,figure=fig)
                return (imgTemp)
            elif (x==3):
                kernel=1/8*np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
                gefiltert=signal.convolve(im,kernel)
                plt.subplot(1, 2, 1)
                plt.title("das originale Bild ")#الصورة الاصلية
                plt.imshow(im, cmap='gray')
                plt.subplot(1, 2, 2)
                plt.title("Das gefilterte Bild (detektion vertikaler Kanten)")#الصورة المفلترة وبالطوي باستخدام كشف الحواف العمودية
                plt.imshow(gefiltert, cmap='gray')
                plt.show()
            elif (x==4):
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
        else :
            print('!!! Error in Image Path')

    def punktoperationen(d,x):#لإنجاز العمليات على العناصر النقطية (البكسل)
        if d != None:
            image = sitk.ReadImage(r"{}".format(d))
            im = sitk.GetArrayFromImage(image)[0, :, :]
                #اي عملية نقطية تريد تنفيذها ...1 للعكس ...2 للقطبية ...3 لتصحيح غاما ..والخيارت الاخرى توقف اللية
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
        else:
            print('!!! Error in Image Path')
