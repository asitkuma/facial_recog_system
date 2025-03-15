from cProfile import label
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
list_of_all_contents=[]
class Attendance_lelo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x780+0+0")
        self.root.title("Welcome_to_attandance Page")
        self.attendace_id=StringVar()
        self.attendance_roll=StringVar()
        self.attendance_name=StringVar()
        self.attendance_dept=StringVar()
        self.attendance_time=StringVar()
        self.attendance_date=StringVar()
        self.present_or_absent=StringVar()

        #bg image
        bg_image=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\5.jpg")
        bg_image=bg_image.resize((1580,780),Image.LANCZOS)
        self.bg_photoimage=ImageTk.PhotoImage(bg_image)
        label_bg=Label(self.root,image=self.bg_photoimage)
        label_bg.place(x=0,y=0,width=1580,height=780)

        img=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\attendance_software_1.jpg")
        img=img.resize((1000,300),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        label=Label(self.root,image=self.photoimage)
        label.place(x=0,y=0,width=750,height=200)

        img2=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\attendance_software_2.jpg")
        img2=img2.resize((1000,300),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label2=Label(self.root,image=self.photoimage2)
        label2.place(x=750,y=0,width=750,height=200)

        label3=Label(self.root,text="ATTENDANCE MANAGEMENT SOFTWARE",bg="Black",fg="red",font=("times-new-roman",30,"bold"))
        label3.place(x=0,y=200,width=1580,height=50)

        frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        frame.place(x=10,y=250,width=1500,height=522)

        #student attendance details
        labelframe_student=LabelFrame(frame,text="Student Attendance Details",bd=2,relief=RIDGE,font=("times-new-roman",12,"bold"),bg="blue")
        labelframe_student.place(x=5,y=0,width=760,height=510)
        
        labelframe_student2=LabelFrame(frame,text="Attendance Details",bd=2,relief=RIDGE,font=("times-new-roman",12,"bold"),bg="white")
        labelframe_student2.place(x=770,y=0,width=722,height=510)

        #photo
        inside_image=Image.open(r"C:\Users\asitk\Desktop\Tkinter_project\inside_attendance.jpg")
        inside_image=inside_image.resize((1000,500),Image.LANCZOS)
        self.photoimage_inside=ImageTk.PhotoImage(inside_image)
        label_image_inside=Label(labelframe_student,image=self.photoimage_inside)
        label_image_inside.place(x=0,y=0,width=760,height=180)

        #entry
        Label1=Label(labelframe_student,text="Attendance Id:-",font=("times-new-roman",12,"bold"),bg="white")
        Label1.place(x=10,y=200)
        entry_1=ttk.Entry(labelframe_student,width=18,font=("times-new-roman",12,"bold"),textvariable=self.attendace_id)
        entry_1.place(x=135,y=200)

        Label2=Label(labelframe_student,text="Roll_Number:-",font=("times-new-roman",12,"bold"),bg="white")
        Label2.place(x=460,y=200)
        entry_2=ttk.Entry(labelframe_student,width=17,font=("times-new-roman",12,"bold"),textvariable=self.attendance_roll)
        entry_2.place(x=582,y=200)

        Label3=Label(labelframe_student,text="Name:-",font=("times-new-roman",12,"bold"),bg="white")
        Label3.place(x=10,y=240)
        entry_3=ttk.Entry(labelframe_student,width=24,font=("times-new-roman",12,"bold"),textvariable=self.attendance_name)
        entry_3.place(x=76,y=240)

        Label4=Label(labelframe_student,text="Department:-",font=("times-new-roman",12,"bold"),bg="white")
        Label4.place(x=460,y=240)
        entry_4=ttk.Entry(labelframe_student,width=18,font=("times-new-roman",12,"bold"),textvariable=self.attendance_dept)
        entry_4.place(x=570,y=240)
        #time

        Label12=Label(labelframe_student,text="Time:-",font=("times-new-roman",12,"bold"),bg="white")
        Label12.place(x=10,y=280)
        entry_12=ttk.Entry(labelframe_student,width=25,font=("times-new-roman",12,"bold"),textvariable=self.attendance_time)
        entry_12.place(x=70,y=280)

        Label4_date=Label(labelframe_student,text="Date:-",font=("times-new-roman",12,"bold"),bg="white")
        Label4_date.place(x=460,y=280)

        entry_16=ttk.Entry(labelframe_student,width=24,font=("times-new-roman",12,"bold"),textvariable=self.attendance_date)
        entry_16.place(x=518,y=280)

        attendance_status=Label(labelframe_student,text="Attendance Status:-",font=("times-new-roman",12,"bold"),bg="white")
        attendance_status.place(x=10,y=320)

        entry_17=ttk.Entry(labelframe_student,width=18,font=("times-new-roman",12,"bold"),textvariable=self.present_or_absent)
        entry_17.place(x=170,y=320)
        
        #4buttons
        make_button_1 = Button(labelframe_student, text="Import CSV", font=(
        "times new roman", 15, "bold"),width=14,bg="black", fg="red",command=self.importCsv)
        make_button_1.place(x=10,y=390)

        make_button_2= Button(labelframe_student, text="export CSV", font=(
        "times new ro2man", 15, "bold"),width=14,bg="black", fg="red",command=self.Export_csv)
        make_button_2.place(x=193,y=390)

        make_button_3= Button(labelframe_student, text="Update", font=(
        "times new ro2man", 15, "bold"),width=14,bg="black", fg="red")
        make_button_3.place(x=377,y=390)

        make_button_3= Button(labelframe_student, text="Reset", font=(
        "times new ro2man", 15, "bold"),width=14,bg="black", fg="red")
        make_button_3.place(x=560,y=390)

        #labelframe right side
        frame_on_right_side=Frame(labelframe_student2,bd=2,relief=RIDGE,bg="white")
        frame_on_right_side.place(x=5,y=5,width=710,height=468)
        
        #create scroll bar
        scroll_x=ttk.Scrollbar(frame_on_right_side,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frame_on_right_side,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(frame_on_right_side,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #now pack this scroll
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        #config means now we will add the data or u can say fir the data to our table
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="StudentId")
        self.AttendanceReportTable.heading("roll",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        #small problem that in the left hand side a space is coming now we can overcome this error by using a function
        self.AttendanceReportTable["show"]="headings" #this will delete that left handi side space

        #now equalizing the width
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

    #Fetch data.....
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    def importCsv(self):
        global list_of_all_contents
        list_of_all_contents.clear()
        #becaz file in our currentcwd
        #*csv is nothg but it is an extension
        #for opening in same window we will use parent=self.root
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(filename) as file:
            csv_read=csv.reader(file,delimiter=",")
            for i in csv_read:
                list_of_all_contents.append(i)
        self.fetch_data(list_of_all_contents)
    def Export_csv(self):
        #save my data into a new file..
        #first check if nothg is there in table
        try:
            if len(list_of_all_contents)==0:
                messagebox.showerror("Some error occured","There is Nothing in there Table :( Try next time")
            else:
                filne_name=filedialog.asksaveasfile(initialdir=os.getcwd(),title="Save The Attendance File",filetypes=(("CSV File","*.csv"),("All File","*.*")),defaultextension=".csv",parent=self.root)
                if filne_name:
                    with open(filne_name.name,"w",newline="") as file:
                        write_into_file=csv.writer(file,delimiter=",")
                        for i in list_of_all_contents:
                            write_into_file.writerow(i)
                    messagebox.showinfo("Sucess","Hats OFF to you man Data is exported :)")
        except Exception as e:
            messagebox.showinfo("Error:(",e)
    def print_all_contents_to_table(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        contents=self.AttendanceReportTable.item(cursor_row)
    



if __name__=="__main__":
    root=Tk()
    object=Attendance_lelo(root)
    root.mainloop()