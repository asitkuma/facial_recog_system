# from email.mime import image
from tkinter import *
from tkinter import ttk
from typing_extensions import Self
from PIL import Image,ImageTk
import os
import numpy as np
import cv2
from tkinter import messagebox
class Train_Image():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Train Data")
        #creating a local variable
        img=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\train_page_data.jpg")
        img=img.resize((1520,400),Image.LANCZOS)
        #instance variable
        self.photoimage=ImageTk.PhotoImage(img)
        label=Label(self.root,image=self.photoimage)
        label.place(x=0,y=0,width=1520,height=350)

        img2=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\train_data_2nd.jpg")
        img2=img2.resize((1520,400),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label2=Label(self.root,image=self.photoimage2)
        label2.place(x=0,y=410,width=1520,height=400)

        button1=Button(self.root,text="TRAIN DATA",bg="black",fg="Red",cursor="hand2",font=("times-new-roman",35,"bold"),command=self.training)
        button1.place(x=0,y=350,width=1520,height=60)
    def training(self):
        #first store the directory..
        try:

            directory=("userphotos")
            path22=[os.path.join(directory,file) for file in os.listdir(directory)]
            faces=[]
            id=[]
            for image in path22:#main motive of this loop to store all the images with their corresponding ids

                img=Image.open(image).convert('L')#convert the image into gray scale.
                image_array=np.array(img,"uint8")#uint is datatpe
                id1=int(os.path.split(image)[1].split('.')[1])
            faces.append(image_array)
            id.append(id1)
            cv2.imshow("Training Is In Progress",image_array)
            cv2.waitKey(1)==ord('q')
            id=np.array(id)
            classifier=cv2.face.LBPHFaceRecognizer_create()
            classifier.train(faces,id)
            classifier.write("model_trained.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Success","Training Successfully done.",parent=self.root)
        except Exception as e:
            messagebox.showinfo("Some Error Occured",e,parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Train_Image(root)
    root.mainloop()