from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import mysql.connector
from tkinter import messagebox
from time import strftime
import datetime
class Face_Recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Facial Recognization")
        img=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\face_recognizer_left.jpg")
        img=img.resize((800,1000),Image.LANCZOS )
        self.photoimage=ImageTk.PhotoImage(img)
        label=Label(self.root,image=self.photoimage)
        label.place(x=0,y=0,width=790,height=850)

        img2=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\face_recognizer_right.jpg")
        img2=img2.resize((1000,780),Image.LANCZOS )
        self.photoimage2=ImageTk.PhotoImage(img2)
        label2=Label(self.root,image=self.photoimage2)
        label2.place(x=790,y=0,width=860,height=780)

        #********** Face Recognition*********#
        def face_recognition():
            def draw_boundary(image,classifier,scalefactor,min_neighbour,color,text,clf):
                #classifier can detect only 2 color cahnnel image
                gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                #multiscaler means it is helpful for object detection in the image it does not matter u r near to the camera or far from the camera
                features=classifier.detectMultiScale(gray_image,scalefactor,min_neighbour)
                print(features)# it will give u a list of length 4
                for(x,y,w,h) in features:
                    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #*****#this is my major disadvantage
                    #algorithm use local binary pattern histogram
                    #fetch the data from mysql db
                    conn = mysql.connector.connect(
                    host="localhost", user="root", password="12345678", database="data")
                    cursor=conn.cursor()
                    #remember while u entered the entries it should be matched by the number u saved while training ur own classifier
                    cursor.execute("select Student_Name from new_table where StudentID="+str(id))
                    name=cursor.fetchone()
                    if name:
                        name=name[0]
                    cursor.execute(f"select Roll_Number from new_table where StudentID="+str(id))
                    roll=cursor.fetchone()
                    if roll:
                        roll=roll[0]
                    cursor.execute(f"select Department from new_table where StudentID="+str(id))
                    dept=cursor.fetchone()
                    if dept:
                        dept=dept[0]


                    #now we will put actual text one the image
                    confidence=int(100*(1-predict/300))
                    if confidence>75:#which can be enhanced by using neural network
                        cv2.putText(image,f"Name:-{name}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                        cv2.putText(image,f"Roll:-{roll}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)

                        with open("present_absent.csv","r") as file:
                            all_data=file.readlines()
                        
                        for i in range(len(all_data)):
                            all_data[i]=all_data[i].replace("\n","")

                        
                        str1 = str(datetime.datetime.now())
                        l1 = str1.split(sep=" ")
                        l2 = l1[0].split(sep="-")
                        l3 = l1[1].split(sep=":")
                        l2.reverse()
                        l4 = l3[-1].split(sep=".")
                        l3[-1] = l4[0]
                        my_date = "/".join(l2)
                        my_time = ":".join(l3)

                        bool_is_true=False
                        for i in all_data:
                            if name in i:
                                bool_is_true=True

                        if not bool_is_true:
                            with open("present_absent.csv","a") as file:
                                file.write(f"{str(id)},{roll},{name},{dept},{my_time},{my_date},present")
                     
                    else:
                       cv2.putText(image,"Unknown",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
                    coardinates=[x,y,w,h]
                    return coardinates
            def recognize(image,clf,facecascade):
                coardinates=draw_boundary(image,facecascade,1.1,8,(255,0,255),"Face",clf)
                return image
            facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")      #face detection
            clf=cv2.face.LBPHFaceRecognizer_create()  
            clf.read("model_trained.xml")

            #now everything is done
            cap=cv2.VideoCapture(0)
            while cap.isOpened():
                ret,frame=cap.read()
                image=recognize(frame,clf,facecascade)
                cv2.imshow("Face Recognizer",frame)
                if cv2.waitKey(1)==ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()

        b1=Button(self.root,text="Click Here",cursor="hand1",font=("times-new-roman",30,"bold"),fg="red",bg="black",command=face_recognition)
        b1.place(x=650,y=690,width=200,height=50)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognizer(root)
    root.mainloop()