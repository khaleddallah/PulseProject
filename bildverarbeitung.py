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
            plt.imshow(im,cmap="gray")
            plt.hist(im.flatten(),bins=10)
            imgTemp="tmp.png"
            plt.savefig(imgTemp, bbox_inches='tight',transparent=True)
            plt.cla()                 
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
                plt.imshow(gefiltert,cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight', transparent=True , pad_inches=0)
                plt.cla()
                return (imgTemp)

            elif (x==2):
                binfilter=1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
                gefiltert=signal.convolve(im,binfilter)
                plt.imshow(gefiltert, cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True)
                plt.cla()
                return (imgTemp)

            elif (x==3):
                kernel=1/8*np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
                gefiltert=signal.convolve(im,kernel)
                plt.imshow(gefiltert, cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0)
                plt.cla()                 
                return (imgTemp)

            elif (x==4):
                kernel=1/8*np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
                gefiltert=signal.convolve(im,kernel)
                plt.imshow(gefiltert, cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0)
                plt.cla()                 
                return (imgTemp)
            else :
                print("Die Prosses wurde beendet")#العملية انهيت
        else :
            print('!!! Error in Image Path')

    def punktoperationen(d,x,par):#لإنجاز العمليات على العناصر النقطية (البكسل)
        if d != None:
            image = sitk.ReadImage(r"{}".format(d))
            im = sitk.GetArrayFromImage(image)[ :, :,0]
            #اي عملية نقطية تريد تنفيذها ...1 للعكس ...2 للقطبية ...3 لتصحيح غاما ..والخيارت الاخرى توقف اللية
            if x==1:
                maxwert=np.max(im)
                neu=maxwert-im
                plt.imshow(neu,cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0, dpi=1000)
                plt.cla()                 
                return (imgTemp)

            elif x==2:
                neu=(im>=par)*np.max(im)
                plt.imshow(neu, cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0)
                plt.cla()                 
                return (imgTemp)

            elif x==3:
                neu = np.max(im)*(im/ np.max(im))**(1/par)
                plt.imshow(neu, cmap='gray')
                imgTemp="tmp.png"
                plt.axis("off")
                plt.savefig(imgTemp, bbox_inches='tight',transparent=True, pad_inches=0)
                plt.cla()                 
                return (imgTemp)

            else:
                print("Die Prosses wurde beendet")#العملية تم انهاؤها
        else:
            print('!!! Error in Image Path')
