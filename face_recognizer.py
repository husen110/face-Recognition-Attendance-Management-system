from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from time import strftime
import cv2
import os
import numpy as np

class Face_recgnition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Student")

        title_lbl=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="WHITE",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1537,height=45)


        img_top=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\std_img.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)


        img_bottom=Image.open(r"C:\Users\hussein\OneDrive\Desktop\face_recognition_system\college_images\std_img.jpg")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)


        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white",command=self.face_recog,)
        b1_1.place(x=365,y=600,width=200,height=60)


    #attendance button
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



  #face recognization button
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="#$$@In5123",database="face_recognizer")
                my_cursor=conn.cursor()



# # Fetch Name,conn = mysql.connector.connect(host="localhost", username="root", password="#$$@In5123", database="face_recognizer")
            
        
    # ✅ Si        ngle query for Name, Roll, Dep
                my_cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id=%s", (id,))
                result = my_cursor.fetchone()
        
                if result:
                      r, n, d, i = result
                else:
                   r, n, d, i = "Unknown", "Unknown", "Unknown"
        
                conn.commit()
                
                conn.close()
                

                if confidence>77:
                    cv2.putText(img,f"ID{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
               

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img,coord
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img,coord=recognize(img,clf,faceCascade)

            cv2.imshow("Welcome To Face Recognition",img)



            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    


if __name__ == "__main__":
    root=Tk()
    obj=Face_recgnition_System(root)
    root.mainloop()
