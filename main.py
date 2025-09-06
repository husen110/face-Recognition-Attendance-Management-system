from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student 
from train import Train
from face_recognizer import Face_recgnition_System
import os
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image

        img =Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\frs_img.jpg")
        img=img.resize((517,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=517,height=130)

        # second image
        img1=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\frs_img1.webp")
        img1=img1.resize((540,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=517,y=0,width=540,height=130)

        # third image
        img2=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\frs_img2.jpg")
        img2=img2.resize((540,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1057,y=0,width=520,height=130)


        # background image
        img3=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\bg_img.jpg")
        img3=img3.resize((1537,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1537,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1537,height=45)

       
 # student button
        img4=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\std_img.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)  

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40) 

    # detect face button
    
        img5=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\fd.webp")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)  

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40) 

     # attendence face button
    
        img6=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\atd_img.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b3.place(x=800,y=100,width=220,height=220)  

        b3_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40) 

    
     # help button
    
        img7=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=1100,y=100,width=220,height=220)  

        b3_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b3_1.place(x=1100,y=300,width=220,height=40) 

    # secound row buttons
    # train face button
        img8=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)  

        b4_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b4_1.place(x=200,y=600,width=220,height=40)

        # photos button
        img9=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\photo.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b5.place(x=500,y=400,width=220,height=220)

        b5_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b5_1.place(x=500,y=600,width=220,height=40)

        # developer button  
        img10=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\dev.webp")   
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=800,y=400,width=220,height=220)

        b6_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b6_1.place(x=800,y=600,width=220,height=40)

        # exit button
        img11=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=1100,y=400,width=220,height=220)

        b7_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
        b7_1.place(x=1100,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")
   #function button

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_recgnition_System(self.new_window)

    def attendence(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)
    

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

