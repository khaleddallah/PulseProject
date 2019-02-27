import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

class a:
    def s(d,x):#لطوي الصورة باستخدام فلاتر مختلفة
        if d != None:

            #اختر المعالجة المرغوبة ....1 لفلتر التوسيط , 2 لفلتر القطبية ,3 لكشف الحواف العمودية ,لكشف الحواف الافقية
            if (x==1):
                image=sitk.ReadImage(r'{}'.format(d))
                im=sitk.GetArrayFromImage(image)[:,:,0]
                kernel=1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])
                gefiltert=signal.convolve(im,kernel)
                plt.imshow(gefiltert,cmap='gray')
                plt.axis("off")
                plt.savefig("tmp11m.jpg", bbox_inches='tight', transparent=True , pad_inches=0)
                plt.cla()
                return ("tmp11.jpg")

a.s("image.jpg",1)
# def bildhistugram(d):#لحساب هيستوغرام الصورة واظهاره
#     if (d!=None):
#         image=sitk.ReadImage(r'{}'.format(d))
#         im=sitk.GetArrayFromImage(image)[:,:,0]
#         kernel=1/8*np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
#         gefiltert=signal.convolve(im,kernel)
        
#         fig = plt.figure(frameon=False)
#         ax = fig.add_axes([0, 0, 1, 1])
#         ax.axis('off')
#         # plt.title("Das gefilterte Bild (detektion vertikaler Kanten)")#الصورة المفلترة وبالطوي باستخدام كشف الحواف العمودية

#         plt.imshow(gefiltert, cmap='gray',figure=fig)
#         # plt.show()
#         imgTemp="tmp1.jpg"
#         plt.savefig(imgTemp, transparent=True, pad_inches=0,figure=fig)
#         # return (imgTemp)
#     else :
#         print('!!! Error in Image Path')

# bildhistugram("image.jpg")
