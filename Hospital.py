from tkinter import*
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox 

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management Syatem")
        self.root.geometry("1540x800+0+0")
        
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurthurInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.BloodPressure=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientID=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        
        
        lbltitle=Label(self.root,text="HOSPITAL MANAGEMENT SYSTEM",relief=RIDGE,bg="white",fg="red",bd=20,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
#-------------------dataframe
        Dataframe=Frame(self.root,bd=12,padx=20,bg="white",relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)


 #-------------------leftdataframe
        DataFrameLeft=LabelFrame(Dataframe,text="PATIENT INFO",relief=RIDGE,fg="black",bd=12,font=("times new roman",12))
        DataFrameLeft.place(x=0,y=5,width=980,height=400)

        lblTablet=Label(DataFrameLeft,text="Tablet Name",font=("times new roman",15,"bold"))
        lblTablet.grid(row=0,column=0,sticky=W,padx=2,pady=6)
        

        
        
        txtref=Entry(DataFrameLeft,textvariable=self.Nameoftablets,font=("times new roman",15,"bold"),width=29)
        txtref.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,text="Reference No.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        #entrybox to enter info
        txtref=Entry(DataFrameLeft,textvariable=self.ref,font=("times new roman",15,"bold"),width=29)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,text="Dose",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        #entrybox to enter info
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("times new roman",15,"bold"),width=29)
        txtDose.grid(row=2,column=1)


        lblNooftablets=Label(DataFrameLeft,text="No. of tablets",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        #entrybox to enter info
        txtNooftablets=Entry(DataFrameLeft,textvariable=self.NumberOfTablets,font=("times new roman",15,"bold"),width=29)
        txtNooftablets.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,text="Lot",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        #entrybox to enter info
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("times new roman",15,"bold"),width=29)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,text="Issue Date",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        #entrybox to enter info
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.Issuedate,font=("times new roman",15,"bold"),width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,text="ExpDate",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        #entrybox to enter info
        txtExpDate=Entry(DataFrameLeft,textvariable=self.Expdate,font=("times new roman",15,"bold"),width=29)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,text="Daily Dose",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        #entrybox to enter info
        txtDailyDose=Entry(DataFrameLeft,textvariable=self.DailyDose,font=("times new roman",15,"bold"),width=29)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,text="Side Effect",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        #entrybox to enter info
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect,font=("times new roman",15,"bold"),width=29)
        txtSideEffect.grid(row=8,column=1)


        lblFurtherInfo=Label(DataFrameLeft,text="Further Info",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        #entrybox to enter info
        txtFurtherInfo=Entry(DataFrameLeft,textvariable=self.FurthurInformation,font=("times new roman",15,"bold"),width=29)
        txtFurtherInfo.grid(row=0,column=3)

       

        lblBloodPressure=Label(DataFrameLeft,text="Blood Pressure",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        #entrybox to enter info
        txtBloodPressure=Entry(DataFrameLeft,textvariable=self.BloodPressure,font=("times new roman",15,"bold"),width=29)
        txtBloodPressure.grid(row=1,column=3)

        lblStorageadvice=Label(DataFrameLeft,text="Storage advice",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblStorageadvice.grid(row=2,column=2,sticky=W)
        #entrybox to enter info
        txtStorageadvice=Entry(DataFrameLeft,textvariable=self.StorageAdvice,font=("times new roman",15,"bold"),width=29)
        txtStorageadvice.grid(row=2,column=3)

        lblMedication=Label(DataFrameLeft,text="Medication",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        #entrybox to enter info
        txtMedication=Entry(DataFrameLeft,textvariable=self.HowToUseMedication,font=("times new roman",15,"bold"),width=29)
        txtMedication.grid(row=3,column=3)

        lblPatientId=Label(DataFrameLeft,text="Patient Id",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        #entrybox to enter info
        txtPatientId=Entry(DataFrameLeft,textvariable=self.PatientID,font=("times new roman",15,"bold"),width=29)
        txtPatientId.grid(row=4,column=3)

        lblNHSNumber=Label(DataFrameLeft,text="NHS Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        #entrybox to enter info
        txtNHSNumber=Entry(DataFrameLeft,textvariable=self.nhsNumber,font=("times new roman",15,"bold"),width=29)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,text="Patient Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        #entrybox to enter info
        txtPatientName=Entry(DataFrameLeft,textvariable=self.PatientName,font=("times new roman",15,"bold"),width=29)
        txtPatientName.grid(row=6,column=3)

        lblDOB=Label(DataFrameLeft,text="DOB",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        #entrybox to enter info
        txtDOB=Entry(DataFrameLeft,textvariable=self.DateOfBirth,font=("times new roman",15,"bold"),width=29)
        txtDOB.grid(row=7,column=3)

        lblPatientAdress=Label(DataFrameLeft,text="Patient Adress",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPatientAdress.grid(row=8,column=2,sticky=W)
        #entrybox to enter info
        txtPatientAdress=Entry(DataFrameLeft,textvariable=self.PatientAddress,font=("times new roman",15,"bold"),width=29)
        txtPatientAdress.grid(row=8,column=3)
        
        
        
#-----------------------right data frame
        DataFrameRight=LabelFrame(Dataframe,text="PRESCRIPTION",relief=RIDGE,fg="black",bd=12,font=("times new roman",12))
        DataFrameRight.place(x=910,y=5,width=550,height=390)   

        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=57,height=17.5,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        #-----------buttons frame----------
        framebuttons=Frame(self.root,bd=10,padx=20,relief=RIDGE)
        framebuttons.place(x=0,y=530,width=1530,height=70)
        
        btnPrescription=Button(framebuttons,command=self.iPrectioption,text="PRESCRIPTION",font=("times new roman",12,"bold"),width=24,bg="green",fg="white")
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(framebuttons,text="PRESCRIPTION DATA",command=self.iPrescriptionData,font=("times new roman",12,"bold"),width=24,bg="green",fg="white")
        btnPrescriptionData.grid(row=0,column=1)

        btnupdate=Button(framebuttons,text="UPDATE",command=self.update,font=("times new roman",12,"bold"),width=24,bg="green",fg="white")
        btnupdate.grid(row=0,column=2)

        btndelete=Button(framebuttons,text="DELETE",command=self.delete,font=("times new roman",12,"bold"),width=24,bg="green",fg="white")
        btndelete.grid(row=0,column=3)

        btnClear=Button(framebuttons,command=self.clear,text="CLEAR",font=("times new roman",12,"bold"),width=22   ,bg="green",fg="white")
        btnClear.grid(row=0,column=4)

        btnexit=Button(framebuttons,text="EXIT",command=self.iexit,font=("times new roman",12,"bold"),width=26,bg="green",fg="white")
        btnexit.grid(row=0,column=5)    
        
        #-----------------table---------------------------
        
        
        Detailsframe=Frame(self.root,bd=12,padx=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1350,height=120)

        
        Table_frame=Frame(Detailsframe,bd=6,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1350,height=110)
        #--------------------scroll bar--------------------
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)  
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","sideeffect","furtherinfo","bloodpressure","storage","medication","pid","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)    
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Referance Number")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("furtherinfo",text="Further Info")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("medication",text="Medication")
        self.hospital_table.heading("pid",text="Patient ID")
        self.hospital_table.heading("nhsnumber",text="NHS number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("sideeffect",width=100)
        self.hospital_table.column("furtherinfo",width=100)
        self.hospital_table.column("bloodpressure",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("medication",width=100)
        self.hospital_table.column("pid",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
       
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        #========FUNCTIONALITY DECLARATION==================
        
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
                messagebox.showerror("Error","All Fields are required")
                
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Harshal@2022",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                            self.Nameoftablets.get(),
                                                                                                            self.ref.get(),
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberOfTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.Expdate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.sideEffect.get(),
                                                                                                            self.FurthurInformation.get(),
                                                                                                            self.StorageAdvice.get(),
                                                                                                            self.BloodPressure.get(),
                                                                                                            self.HowToUseMedication.get(),
                                                                                                            self.PatientID.get(),
                                                                                                            self.nhsNumber.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.PatientAddress.get() 
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("success","Record has been inserted succesfully")
                                                                                              
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)        
                                     

    
    
    
    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Harshal@2022",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NameOfTablet=%s, dose=%s, Numbersoftablet=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, sideEffect=%s, furtherInfo=%s, BloodPressure=%s, StorageAdv=%s, medication=%s, patientID=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where ReferenceNo=%s ",(
                                                                                                            self.Nameoftablets.get(),
                                                                                                            
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberOfTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.Expdate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.sideEffect.get(),
                                                                                                            self.FurthurInformation.get(),
                                                                                                            self.StorageAdvice.get(),
                                                                                                            self.BloodPressure.get(),
                                                                                                            self.HowToUseMedication.get(),
                                                                                                            self.PatientID.get(),
                                                                                                            self.nhsNumber.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.PatientAddress.get(),
                                                                                                            self.ref.get(), 
            
        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Update","Record has been updated succesfully")
        
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Harshal@2022",database="mydata")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
                
            conn.commit()
        conn.close()
    
    
    
    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"] 
        
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEffect.set(row[8])
        self.FurthurInformation.set(row[9])        
        self.BloodPressure.set(row[10])
        self.StorageAdvice.set(row[11])
        self.HowToUseMedication.set(row[12])
        self.PatientID.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])


    
    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get() +"\n")
        self.txtPrescription.insert(END,"Refernce No:\t\t\t"+self.ref.get() +"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get() +"\n")
        self.txtPrescription.insert(END,"Number Of Tabets:\t\t\t"+self.NumberOfTablets.get() +"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get() +"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get() +"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get() +"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get() +"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get() +"\n")
        self.txtPrescription.insert(END,"Further information:\t\t\t"+self.FurthurInformation.get() +"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.BloodPressure.get() +"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get() +"\n")
        self.txtPrescription.insert(END,"Medication:\t\t\t"+self.HowToUseMedication.get() +"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientID.get() +"\n")
        self.txtPrescription.insert(END,"NHS No:\t\t\t"+self.nhsNumber.get() +"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get() +"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get() +"\n")


    
    def delete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Harshal@2022",database="mydata")
        my_cursor=conn.cursor()
        query = "delete from hospital where ReferenceNo = %s"
        value = (self.ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been removed from database!!")
        

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurthurInformation.set("")
        self.StorageAdvice.set("")
        self.BloodPressure.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set('')
        self.DateOfBirth.set("")
        self.PatientAddress.set("") 
        self.txtPrescription.delete("1.0",END)

                                                                                                           
    def iexit(self):
        iexit= messagebox.askyesno("Hospital Management System", "Confirm you want to exit or not")
        if iexit>0:
            root.destroy()
            return
                                    
                                  
                                  
                                  
                                  
                
            
        
        
root=Tk()
ob=Hospital(root)
root.mainloop()