from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import tkinter.font as font

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Attendance")

        img =Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\std1.webp")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # second image
        img1=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\std2.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # background image


        img3=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\bg_img.jpg")
        img3=img3.resize((1537,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1537,height=590)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1537,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=500)

        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=480)

        img_left=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\atd_img.jpg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) 

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=300)



     #label and entry
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5)

        #name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5)

        name_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold")) 
        name_entry.grid(row=0,column=3,padx=10,pady=5)

        #date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=1,column=0,padx=10,pady=5)

        date_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))     
        date_entry.grid(row=1,column=1,padx=10,pady=5)

        #department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5)

        dep_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))     
        dep_entry.grid(row=1,column=3,padx=10,pady=5)

        #time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5)  

        time_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))     
        time_entry.grid(row=2,column=1,padx=10,pady=5)

        #attendance
        attend_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attend_label.grid(row=3,column=0,padx=10,pady=5)    

        self.attend_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=3,column=1,padx=10,pady=5)


        #button 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white") 
        btn_frame.place(x=0,y=200,width=715,height=35)

        b1_1=Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        b1_1.grid(row=0,column=0)

        b1_2=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=17,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        b1_2.grid(row=0,column=1)

        b1_3=Button(btn_frame,text="Update",width=17,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")     
        b1_3.grid(row=0,column=2)

        b1_4=Button(btn_frame,text="Reset",width=17,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")     
        b1_4.grid(row=0,column=3)


        #right label frame
        Right_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white") 
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=750,y=10,width=710,height=500 )


######### scroll bar table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendance_table=ttk.Treeview(table_frame,column=("id","name","date","dep","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("id",text="Attendance ID")
        self.Attendance_table.heading("name",text="Name")
        self.Attendance_table.heading("date",text="Date")
        self.Attendance_table.heading("dep",text="Department")  
        self.Attendance_table.heading("time",text="Time")
        self.Attendance_table.heading("attendance",text="Attendance Status")

        self.Attendance_table["show"]="headings"

        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("dep",width=100)
        self.Attendance_table.column("time",width=100)
        self.Attendance_table.column("attendance",width=100)

        self.Attendance_table.pack(fill=BOTH,expand=1)

    def fetchData(self,rows):
            self.Attendance_table.delete(*self.Attendance_table.get_children())
            for i in rows:
                self.Attendance_table.insert("",END,values=i)

    def importCsv(self):
        global mydata

        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
             mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
             if len(mydata)<1:
                 messagebox.showerror("No Data","No Data found to export",parent=self.root)
                 return False

             fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
             with open(fln,mode="w",newline="") as myfile:
                 exp_write=csv.writer(myfile,delimiter=",")
                 for i in mydata:
                     exp_write.writerow(i)
                 messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")    
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
       



        #right frame
       




if __name__ == "__main__":
            root=Tk()
            obj=Attendance(root)
            root.mainloop()