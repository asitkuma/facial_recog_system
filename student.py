from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

global_choose_student_id_from_table=None

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x780+0+0")
        self.root.title("Student Detail Page")
        # variable=============================//store..
        self.dep = StringVar()
        # string var is an class and we initializing it..
        self.cour = StringVar()
        self.yr = StringVar()
        self.sem = StringVar()
        self.s_id = StringVar()
        self.s_name = StringVar()
        self.Blogs = StringVar()
        self.R_no = StringVar()
        self.gender = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.p_number = StringVar()
        self.email = StringVar()
        self.t_name = StringVar()
        self.radio1 = StringVar()
        self.radio1.set(None)

        # creating a local variable.
        img = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\student_image1.jpeg")
        img = img.resize((530, 130), Image.LANCZOS)
        # instance variable
        self.photoimage = ImageTk.PhotoImage(img)
        label = Label(self.root, image=self.photoimage)
        label.place(x=0, y=0, width=530, height=130)

        img2 = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\student_image_2.png")
        img2 = img2.resize((580, 130), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        label1 = Label(self.root, image=self.photoimage2)
        label1.place(x=530, y=0, width=560, height=130)

        img3 = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\student3.jpg")
        img3 = img3.resize((560, 130), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        label2 = Label(self.root, image=self.photoimage3)
        label2.place(x=1020, y=0, width=550, height=130)

        img4 = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\fancy.jpg")
        img4 = img4.resize((1520, 650), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        label3 = Label(self.root, image=self.photoimage4)
        label3.place(x=0, y=130, width=1520, height=650)

        heading = Label(label3, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="Blue", fg="white")
        heading.place(x=0, y=0, width=1520, height=40)

        frame1 = Frame(label3, bd=2, bg="white")
        frame1.place(x=15, y=43, width=1520, height=650)

        # left label frame

        left_frame = LabelFrame(frame1, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=(
            "times new roman", 12, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=760, height=580)

        right_frame = LabelFrame(frame1, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=(
            "times new roman", 12, "bold"), bg="white")
        right_frame.place(x=780, y=10, width=710, height=580)

        # creating image inside the left frame
        left_frame_image = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\student_image.jpg")
        left_frame_image = left_frame_image.resize((758, 130), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(left_frame_image)

        image_label = Label(left_frame, image=self.photoimage5)
        image_label.place(x=5, y=0, width=755, height=130)

        # labelframe inside the left frame
        course_related_frame = LabelFrame(left_frame, bd=2, text="CURRENT COURSE INFORMATION", font=(
            "times new roman", 12, "bold"), bg="white")
        course_related_frame.place(x=5, y=138, width=750, height=135)

        # inside course related frame...we neefd to ceate grid .in grid there is rows and columns.so whenever we ned to change we need to change the frame completely thats why grid.
        label_inside_lblframe = Label(course_related_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        label_inside_lblframe.grid(row=0, column=0, padx=10, pady=10)
        # create combo box
        combo_1 = ttk.Combobox(course_related_frame, textvariable=self.dep, font=(
            "times new roman", 12, "bold"), width=18, state="readonly")
        combo_1.grid(row=0, column=1, padx=10, pady=10)
        combo_1["values"] = ("Select Department", "CSE/COE/AL&ML..",
                             "Civil", "Electrical", "Mechanical", "Any others")
        combo_1.current(0)
        # &&/

        course_related = Label(course_related_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_related.grid(row=0, column=3, padx=10, pady=10)
        combo_2 = ttk.Combobox(course_related_frame, textvariable=self.cour, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        combo_2["values"] = ("Select Your Course",
                             "BTech", "Mtech", "Any others")
        combo_2.current(0)
        combo_2.grid(row=0, column=4, padx=10, pady=10)

        year = Label(course_related_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year.grid(row=1, column=0, padx=10, pady=10)
        combo_3 = ttk.Combobox(course_related_frame, textvariable=self.yr, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        combo_3["values"] = ("Select Your Year", "<2020",
                             "2021", "2022", "2023", ">=2024")
        combo_3.current(0)
        combo_3.grid(row=1, column=1, padx=10, pady=10)

        Year = Label(course_related_frame, text="Semester",
                     font=("times new roman", 12, "bold"), bg="white")
        Year.grid(row=1, column=3, padx=10, pady=10)
        combo_4 = ttk.Combobox(course_related_frame, textvariable=self.sem, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        combo_4["values"] = ("Semester", "1", "2", "3",
                             "4", "5", "6", "7", "8")
        combo_4.current(0)
        combo_4.grid(row=1, column=4, padx=10, pady=10)

        class_student_information = LabelFrame(frame1, text="STUDENT INFORMATION", bd=2, relief=RIDGE, font=(
            "times new roman", 12, "bold"), bg="white")
        class_student_information.place(x=17, y=308, width=748, height=276)
        
        # entry inside the spaces

        student_id_label = Label(class_student_information, text="StudentID", font=(
            "times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=7, pady=7)
        student_id_entry = ttk.Entry(class_student_information, textvariable=self.s_id, font=(
            "times new roman", 12, "bold"), width=18)
        student_id_entry.grid(row=0, column=1, padx=7, pady=7)

        backlog_label = Label(class_student_information, text="No Of Backlogs", font=(
            "times new roman", 12, "bold"), bg="white")
        backlog_label.grid(row=1, column=0, padx=10, pady=10)

        backlog_entery = ttk.Entry(class_student_information, textvariable=self.Blogs, font=(
            "times new roman", 12, "bold"), width=18)
        backlog_entery.grid(row=1, column=1, padx=7, pady=7)

        gender_label = Label(class_student_information, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=7, pady=7)
        gender_entery = ttk.Entry(class_student_information, textvariable=self.gender, font=(
            "times new roman", 12, "bold"), width=18)
        gender_entery.grid(row=2, column=1, padx=7, pady=7)

        address_label = Label(class_student_information, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=0, padx=7, pady=7)
        address_entery = ttk.Entry(class_student_information, textvariable=self.address, font=(
            "times new roman", 12, "bold"), width=18)
        address_entery.grid(row=3, column=1, padx=7, pady=7)

        email_label = Label(class_student_information, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")

        email_label.grid(row=4, column=0, padx=7, pady=7)
        email_entery = ttk.Entry(class_student_information, textvariable=self.email, font=(
            "times new roman", 12, "bold"), width=18)
        email_entery.grid(row=4, column=1, padx=7, pady=7)

        student_name_label = Label(class_student_information, text="Student Name", font=(
            "times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=7, pady=7)
        student_name_entery = ttk.Entry(class_student_information, textvariable=self.s_name, font=(
            "times new roman", 12, "bold"), width=18)
        student_name_entery.grid(row=0, column=3, padx=7, pady=7)

        Roll_label = Label(class_student_information, text="Roll Number", font=(
            "times new roman", 12, "bold"), bg="white")
        Roll_label.grid(row=1, column=2, padx=7, pady=7)
        Roll_label_entery = ttk.Entry(class_student_information, textvariable=self.R_no, font=(
            "times new roman", 12, "bold"), width=18)
        Roll_label_entery.grid(row=1, column=3, padx=7, pady=7)

        DOB_label = Label(class_student_information, text="DOB", font=(
            "times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=10)
        DOB_entery = ttk.Entry(class_student_information, textvariable=self.dob, font=(
            "times new roman", 12, "bold"), width=18)
        DOB_entery.grid(row=2, column=3, padx=10, pady=10)

        phone_number_label = Label(class_student_information, text="Phone Number", font=(
            "times new roman", 12, "bold"), bg="white")
        phone_number_label.grid(row=3, column=2, padx=10, pady=10)
        phone_number_entery = ttk.Entry(class_student_information, textvariable=self.p_number, font=(
            "times new roman", 12, "bold"), width=18)
        phone_number_entery.grid(row=3, column=3, padx=10, pady=10)

        Teacher_label = Label(class_student_information, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg="white")
        Teacher_label.grid(row=4, column=2, padx=10, pady=10)
        Teacher_label_entery = ttk.Entry(class_student_information, textvariable=self.t_name, font=(
            "times new roman", 12, "bold"), width=18)
        Teacher_label_entery.grid(row=4, column=3, padx=10, pady=10)

        radio_1 = Radiobutton(class_student_information, variable=self.radio1, text="Take Photo sample", font=(
            "times new roman", 11, "bold"), bg="white", value="Yes")
        radio_1.grid(row=5, column=0)
        radio_2 = Radiobutton(class_student_information, variable=self.radio1, text="Dont Take Photo Sample", font=(
            "times new roman", 11, "bold"), bg="white", value="No")
        radio_2.grid(row=5, column=1)
        buttons_inside_frame = Frame(
            class_student_information, relief=RIDGE, bd=1, bg="white")
        buttons_inside_frame.place(x=654, y=0, width=780, height=253)

        button1 = Button(buttons_inside_frame, command=self.ischeck, text="Save", font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        button1.place(x=0, y=0, width=100, height=42)

        button2 = Button(buttons_inside_frame, text="Update", command=self.update_student_details, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white", width=16, height=2)
        button2.place(x=0, y=42, width=100, height=43)
        button3 = Button(buttons_inside_frame, command=self.delete_option, text="Delete", font=(
            "times new roman", 11, "bold"), bg="blue", fg="white", width=16, height=2)
        button3.place(x=0, y=84, width=100, height=43)
        button4 = Button(buttons_inside_frame, text="Reset", command=self.reset_the_details, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        button4.place(x=0, y=127, width=100, height=45)

        button5 = Button(buttons_inside_frame, command=self.generate_dataset, text="Take\nPhoto", font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        button5.place(x=0, y=166, width=100, height=45)

        button6 = Button(buttons_inside_frame, text="Update\n Photo", font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        button6.place(x=0, y=206, width=100, height=46)
        # right side image
        right_frame_image = Image.open(
            r"C:\Users\asitk\Desktop\Tkinter_project\right_me_fit_kar.jpg")
        right_frame_image = right_frame_image.resize(
            (748, 130), Image.LANCZOS)
        self.photoimage10 = ImageTk.PhotoImage(right_frame_image)
        label_for_image_right = Label(right_frame, image=self.photoimage10)
        label_for_image_right.place(x=5, y=0, width=700, height=130)
        # create a label frame with name search system..
        course_related_frame = LabelFrame(right_frame, bd=2, text="Search System", font=(
            "times new roman", 12, "bold"), bg="white")
        course_related_frame.place(x=5, y=135, width=700, height=75)
        # inside label frame

        label_inside_search_system = Label(course_related_frame, text="Search By", font=(
            "times new roman", 12, "bold"), fg="white", bg="green", width=12)
        label_inside_search_system.grid(row=0, column=0, pady=8, padx=8)

        combo_box_after_search = ttk.Combobox(course_related_frame, width=17, font=(
            "times new roman", 12, "bold"), state="readonly")
        combo_box_after_search["values"] = ("Roll Number", "Reg Number")
        combo_box_after_search.current(0)
        combo_box_after_search.grid(row=0, column=1)

        make_one_entry = ttk.Entry(course_related_frame, font=(
            "times new roman", 12, "bold"), width=17)
        make_one_entry.grid(row=0, column=2, padx=8)

        make_button_1 = Button(course_related_frame, text="Search", font=(
            "times new roman", 12, "bold"), width=11, bg="blue", fg="white")
        make_button_1.grid(row=0, column=3)
        make_button_2 = Button(course_related_frame, text="Show All", font=(
            "times new roman", 12, "bold"), width=11, bg="blue", fg="white")
        make_button_2.grid(row=0, column=4, padx=4)

        # frame after search
        frame_after_search = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        frame_after_search.place(x=5, y=213, width=698, height=343)
        scroll_x = ttk.Scrollbar(frame_after_search, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame_after_search, orient=VERTICAL)

        self.student_table = ttk.Treeview(frame_after_search, columns=("dep", "course", "year", "Semester", "S_ID", "S_Name", "BackLogs", "RollNumber",
                                          "Gender", "DOB", "Address", "PNumber", "Email", "T_Name", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("S_ID", text="Student ID")
        self.student_table.heading("S_Name", text="Student Name")
        self.student_table.heading("BackLogs", text="Backlogs")
        self.student_table.heading("RollNumber", text="RollNumber")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("PNumber", text="Phone Number")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("T_Name", text="Teacher Name")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("S_ID", width=100)
        self.student_table.column("S_Name", width=100)
        self.student_table.column("BackLogs", width=100)
        self.student_table.column("RollNumber", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("PNumber", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("T_Name", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.point_to_content)
        self.place_data_in_screen()
        # bind the connection with button and the table.
        # #various kind of ButtonRelease are there.

    def ischeck(self):
        if(self.dep.get() == "Select Department" or self.cour.get() == "Select Your Course" or self.yr.get() == "Select Your Year" or self.sem.get() == "Semester" or self.s_id.get() == "" or self.s_name.get() == "" or self.Blogs.get() == "" or self.R_no.get() == "" or self.gender.get() == "" or self.dob.get() == "" or self.address.get() == "" or self.p_number.get() == "" or self.email.get() == "" or self.t_name.get() == ""):
            messagebox.showerror(
                "Error", "All Fields Are Mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="12345678", database="data")
                curs1 = conn.cursor()  # The cursor object allows you to execute SQL queries and retrieve the results.Once you have the cursor object curs1, you can use its methods to interact with the database. For example, you can execute SQL queries by calling curs1.execute(query) or fetch the query results using curs1.fetchall() or curs1.fetchone().
                curs1.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.dep.get(), self.cour.get(), self.yr.get(), self.sem.get(), self.s_id.get(
                ), self.s_name.get(), self.Blogs.get(), self.R_no.get(), self.gender.get(), self.dob.get(), self.address.get(), self.p_number.get(), self.email.get(), self.t_name.get(), self.radio1.get()))
                conn.commit()
                # Here it indicates that in the initial window or in live fetch or print the data
                self.place_data_in_screen()
                conn.close()
                messagebox.showinfo(
                    "success", "You data successfully submitted with us.", parent=self.root)
                self.dep.set("")
                self.cour.set("")
                self.yr.set("")
                self.sem.set("")
                self.s_id.set("")
                self.s_name.set("")
                self.Blogs.set("")
                self.R_no.set("")
                self.gender.set("")
                self.dob.set("")
                self.address.set("")
                self.p_number.set("")
                self.email.set("")
                self.t_name.set("")
                self.radio1.set("")

            except Exception as e:
                messagebox.showinfo(
                    "error",e, parent=self.root)

    def place_data_in_screen(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="12345678", database="data")
        cursor = connection.cursor()
        cursor.execute("select * from new_table")
        data = cursor.fetchall()
        if(len(data) != 0):
            # delete the data which is present in the current window
            self.student_table.delete(*self.student_table.get_children())
            # now fetch the data in that table
            for i in data:
                self.student_table.insert("", END, values=i)
            # the reason of commit is to add data continiously.
            connection.commit()
        connection.close()

    def point_to_content(self, connect_with_button=""):
        # when u will point the content of the data which is present inside the table
        mouse_focus = self.student_table.focus()
        # store all the data insode the variable
        all_items = self.student_table.item(mouse_focus)
        # extracting all values
        var1 = all_items["values"]

        global_choose_student_id_from_table=var1[4]

        # now set one by one
        self.dep.set(var1[0])
        self.cour.set(var1[1])
        self.yr.set(var1[2])
        self.sem.set(var1[3])
        self.s_id.set(var1[4])
        self.s_name.set(var1[5])
        self.Blogs.set(var1[6])
        self.R_no.set(var1[7])
        self.gender.set(var1[8])
        self.dob.set(var1[9])
        self.address.set(var1[10])
        self.p_number.set(var1[11])
        self.email.set(var1[12])
        self.t_name.set(var1[13])
        self.radio1.set(var1[14])

    def update_student_details(self):
        if(self.dep.get() == "Select Department" or self.cour.get() == "Select Your Course" or self.yr.get() == "Select Your Year" or self.sem.get() == "Semester" or self.s_id.get() == "" or self.s_name.get() == "" or self.Blogs.get() == "" or self.R_no.get() == "" or self.gender.get() == "" or self.dob.get() == "" or self.address.get() == "" or self.p_number.get() == "" or self.email.get() == "" or self.t_name.get() == ""):
            messagebox.showerror(
                "Error", "All Fields Are Mandatory", parent=self.root)
        else:
            try:
                # create a connection and delete with the database and update
                update = messagebox.askyesno(
                    "Confirmation", "Do you really want to update?", parent=self.root)
                if update > 0:
                    con1 = mysql.connector.connect(
                        host="localhost", user="root", password="12345678", database="data")

                    cursor1 = con1.cursor()

                    cursor1.execute("update new_table set Department=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Backlogs=%s,Roll_Number=%s,Gender=%s,DOB=%s,Address=%s,PhoneNumber=%s,Email=%s,TeacherName=%s,Photo=%s where StudentID=%s", (self.dep.get(), self.cour.get(
                    ), self.yr.get(), self.sem.get(), self.s_name.get(), self.Blogs.get(), self.R_no.get(), self.gender.get(), self.dob.get(), self.address.get(), self.p_number.get(), self.email.get(), self.t_name.get(), self.radio1.get(), self.s_id.get()))
                else:
                    return messagebox.showinfo("User denied", "Your Information is not deleted", parent=self.root)
                messagebox.showinfo("update Successfull :)", parent=self.root)
                # for continue updation then print in the window and then close.
                con1.commit()
                self.place_data_in_screen()
                con1.close()
            except Exception as e:
                messagebox.showerror("Error", f"some error occured :( {e}")

    def delete_option(self):
        # we need to delete by the primary key so.we chhose student id
        if(self.s_id.get() == ""):
            return messagebox.showwarning("User Student Id is necessary field. :( ", parent=self.root)
        else:
            try:
                strt_conn = mysql.connector.connect(
                    host="localhost", user="root", password="12345678", database="data")
                # object for exceute the quries inside the db.
                cursor1 = strt_conn.cursor()
                sql_query = "delete from new_table where studentID=%s"
                # it will bydefault take two arguement
                value1 = (self.s_id.get(),)
                if value1 != "default":
                    info1 = messagebox.askyesno(
                        "Confirmation", "Do you really want to delete the row")
                    if info1 > 0:
                        cursor1.execute(sql_query, value1)
                        messagebox.showinfo(
                            "Success", "User details deleted :)", parent=self.root)
                    else:
                        messagebox.showinfo(
                            "Access denied", "Your details is not deleted :)", parent=self.root)
            except Exception as e:
                messagebox.showinfo("Error", e, parent=self.root)
        strt_conn.commit()
        self.place_data_in_screen()
        strt_conn.close()

    def reset_the_details(self):
        self.dep.set("Select Department")
        self.cour.set("Select Your Course")
        self.yr.set("Select Your Year")
        self.sem.set("Semester")
        self.s_id.set("")
        self.s_name.set("")
        self.Blogs.set("")
        self.R_no.set("")
        self.gender.set("")
        self.dob.set("")
        self.address.set("")
        self.p_number.set("")
        self.email.set("")
        self.t_name.set(" ")
        self.radio1.set(None)
    # real part of the code......

    def generate_dataset(self):
        if(self.dep.get() == "Select Department" or self.cour.get() == "Select Your Course" or self.yr.get() == "Select Your Year" or self.sem.get() == "Semester" or self.s_id.get() == "" or self.s_name.get() == "" or self.Blogs.get() == "" or self.R_no.get() == "" or self.gender.get() == "" or self.dob.get() == "" or self.address.get() == "" or self.p_number.get() == "" or self.email.get() == "" or self.t_name.get() == ""):
            messagebox.showerror(
                "Error", "All Fields Are Mandatory", parent=self.root)
        else:
            try:
                con1 = mysql.connector.connect(host="localhost", user="root", password="12345678", database="data")
                cursor1 = con1.cursor()
                cursor1.execute("select * from new_table")
                var1 = cursor1.fetchall()
                id = 0
                s_id=[]
                db_s_id=0
                for i in var1:
                    db_s_id=i[4]
                    id += 1
                # what i am thinking that lets update the db.when u will capture the face .in the original db it will update the db.either inserting like present or absent.

                cursor1.execute("update new_table set Department=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Backlogs=%s,Roll_Number=%s,Gender=%s,DOB=%s,Address=%s,PhoneNumber=%s,Email=%s,TeacherName=%s,Photo=%s where StudentID=%s", (self.dep.get(), self.cour.get(
                ), self.yr.get(), self.sem.get(), self.s_name.get(), self.Blogs.get(), self.R_no.get(), self.gender.get(), self.dob.get(), self.address.get(), self.p_number.get(), self.email.get(), self.t_name.get(), self.radio1.get(), self.s_id.get() == id+1))

                con1.commit()
                self.place_data_in_screen()  # invoking the function
                self.reset_the_details()
                con1.close()

                # cascade classifier is basically a class in which the pretrained xml file goes as a parameter.and assign to constructor.now we initialized it.and by the help of an object now we can classifies the image by using the methods of that class.
                object1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_detection(img):
                    # convert RGB to gray scale

                    gray_variable = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    my_face = object1.detectMultiScale(gray_variable, 1.3, 5)
                    # so confused ri8? 1.3 and 5? 1.3 is scalin factor means reduce the size of the image .even in small image it will detect well. and 5 is minimum nieghbour in order to detect  the original face.1.3 means multiple images with diff sizes .it give good accuracy but while predicting it will take more time.
                    # in order to create a rectangle.
                    for(x, y, w, h) in my_face:
                        face_detection = img[y:y+h, x:x+w]
                        return face_detection
                cap = cv2.VideoCapture(0)  # webcam
                count = 0
                while True:
                    # here ret is bool and it is necessary..
                    ret, my_frame = cap.read()
                    var1=face_detection(my_frame)
                    if var1 is not None:
                        count += 1
                        my_face = cv2.resize(var1, (450, 450))  # this is human image
                        my_face = cv2.cvtColor(my_face, cv2.COLOR_BGR2GRAY)
                        if global_choose_student_id_from_table!=None:
                            file_path = "userphotos/user." + str(db_s_id)+"."+str(count)+".jpg"
                            global_choose_student_id_from_table=None
                        else:
                            file_path = "userphotos/user." + str(db_s_id)+"."+str(count)+".jpg"
                        cv2.imwrite(file_path, my_face)
                        # 2 is font scale(small,large) and 3 is thickness(wide)
                        cv2.putText(my_face, str(count), (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 2, (210, 210, 32), 3)
                        cv2.imshow("Recording In Process", my_face)
                    if cv2.waitKey(1) == 13 or count == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Thanks", "Good job :)", parent=self.root)
            except Exception as e:
                messagebox.showinfo("Error", e, parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj2 = student(root)
    root.mainloop()