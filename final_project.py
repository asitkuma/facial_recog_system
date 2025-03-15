from setuptools import command
from tkinter import * #we sre using ttk for croping ot editing purpose..
from tkinter import ttk
from PIL import Image,ImageTk #this is pillow library
# from student import student
import os
# from train_data import Train_Image
# from face_recognizer import Face_Recognizer
# from attendance_software import Attendance_lelo
class attendance_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Facial Recognization")
        #creating a local variable
        img=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\2.jpg")
        img=img.resize((530,130),Image.LANCZOS)
        #instance variable

        self.photoimage=ImageTk.PhotoImage(img)
        label=Label(self.root,image=self.photoimage)
        label.place(x=0,y=0,width=530,height=130)

        img2=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\3.jpeg")
        img2=img2.resize((580,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label1=Label(self.root,image=self.photoimage2)
        label1.place(x=530,y=0,width=560,height=130)

        img3=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\4.jpeg")
        img3=img3.resize((560,130),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        label2=Label(self.root,image=self.photoimage3)
        label2.place(x=1020,y=0,width=550,height=130)


        img4=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\5.jpg")
        img4=img4.resize((1520,650),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        label3=Label(self.root,image=self.photoimage4)
        label3.place(x=0,y=130,width=1520,height=650)

        heading=Label(label3,text="FACE RECOGNIZATION ATTENDANCE SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        heading.place(x=0,y=0,width=1520,height=40)

        
        #buttons
        student_image=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\student_image.jpg")
        student_image=student_image.resize((230,230),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(student_image)

        # command=self.open_student_window,
        b1=Button(label3,image=self.photoimage5,cursor="hand1")
        b1.place(x=150,y=100,width=200,height=200)

        # command=self.open_student_window,
        b2=Button(label3,text="STUDENT DETAILS",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b2.place(x=150,y=300,width=200,height=30)


        #face detector
        face_detector=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\face1.jpg")
        face_detector=face_detector.resize((230,230),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(face_detector)

        # ,command=self.face_detector
        b3=Button(label3,image=self.photoimage6,cursor="hand1")
        b3.place(x=490,y=100,width=200,height=200)

        # ,command=self.face_detector
        b4=Button(label3,text="FACE DETECTOR",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b4.place(x=490,y=300,width=200,height=30)

        #attendance
        attendance=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\attendance.jpg")
        attendance=attendance.resize((230,230),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(attendance)

        # ,command=self.attendance_check
        b5=Button(label3,image=self.photoimage7,cursor="hand1")
        b5.place(x=830,y=100,width=200,height=200)

        # ,command=self.attendance_check
        b6=Button(label3,text="ATTENDANCE",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b6.place(x=830,y=300,width=200,height=30)

        #help desk
        help_desk=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\help_desk.jpg")
        help_desk=help_desk.resize((230,230),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(help_desk)

        b7=Button(label3,image=self.photoimage8,cursor="hand1")
        b7.place(x=1200,y=100,width=200,height=200)

        b8=Button(label3,text="HELP DESK",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b8.place(x=1200,y=300,width=200,height=30)


        #train data
        Train_data=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\train_images.jpg")
        Train_data=Train_data.resize((230,230),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(Train_data)

        # ,command=self.opening_train_window
        b10=Button(label3,image=self.photoimage9,cursor="hand1")
        b10.place(x=150,y=400,width=200,height=200)

        # command=self.opening_train_window
        b11=Button(label3,text="Train Data",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red",)
        b11.place(x=150,y=600,width=200,height=30)



        #photos
        my_image=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\photos.png")
        my_image=my_image.resize((230,230),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(my_image)

        # ,command=self.open_image_folder
        b12=Button(label3,image=self.photoimage10,cursor="hand1")
        b12.place(x=490,y=400,width=200,height=200)

        # ,command=self.open_image_folder
        b13=Button(label3,text="photos",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b13.place(x=490,y=600,width=200,height=30)


        #developer
        developer1=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\developer.jpg")
        developer1=developer1.resize((230,230),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(developer1)

        b14=Button(label3,image=self.photoimage11,cursor="hand1")
        b14.place(x=830,y=400,width=200,height=200)
        b14=Button(label3,text="Developer",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b14.place(x=830,y=600,width=200,height=30)


        #Exit
        exit=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\exit.png")
        exit=exit.resize((230,230),Image.LANCZOS)
        self.photoimage12=ImageTk.PhotoImage(exit)

        b15=Button(label3,image=self.photoimage12,cursor="hand1")
        b15.place(x=1200,y=400,width=200,height=200)
        b14=Button(label3,text="Exit",cursor="hand1",font=("European",14,"bold"),bg="black",fg="red")
        b14.place(x=1200,y=600,width=200,height=30)

    # def open_image_folder(self):
    #     os.startfile("userphotos")

    # def open_student_window(self):
    #     self.new_window=Toplevel(self.root)#this means that new window will come on the top of root window
    #     self.open=student(self.new_window)

    # def opening_train_window(self):
    #     self.new_window=Toplevel(self.root)
    #     self.open=Train_Image(self.new_window)
    # def face_detector(self):
    #     self.new_window=Toplevel(self.root)
    #     self.open=Face_Recognizer(self.new_window)
    
    # def attendance_check(self):
    #     self.new_window=Toplevel(self.root)
    #     self.open=Attendance_lelo(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=attendance_system(root)
    root.mainloop()