import tkinter as tk                # python 3
from tkinter import *
from tkinter import messagebox
from tkinter import font  as tkfont# python 3
import tkinter.ttk as ttk
import webbrowser
from reportlab.pdfgen import canvas
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
#****************************************

#connecting to the database
import mysql.connector
import mysql
mydb=mysql.connector.connect(
    host="localhost",user="root",password="icec00l",database='jointh-c')


class JoinTh_c(tk.Tk):
    def __init__(self, *args, **kwargs):
    
        tk.Tk.__init__(self, *args, **kwargs)
        global container
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        #self.geometry("600x450+720+140")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")
        
        self.title("JoinTh-C")
        container = tk.Frame(self)
        container.configure(background="#d9d9d9")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,Main,parent,children,worker,event,saving,search,report):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


        
        
################ PARENT CALL FUNCTIONS ################################################################################################      

    def helper(self,self1):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Parents_id FROM Parents")
        myr=mycursor.fetchall()
        for x in myr:
            self1.TCombobox2['value']=(myr)
        

    def showp(self,self1):
        self1.Listbox0.delete(0,self1.Listbox0.size())
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from parents")
        rows = cursor.fetchall()
        
        for row in rows:
            self1.Listbox0.insert(1,row)
            
            
    def addParent(self,self1):
        first=self1.TextFirst1.get('1.0', 'end-1c')
        last=self1.TextLast1.get('1.0', 'end-1c')
        address1=self1.TextAddress1P.get('1.0', 'end-1c')
        address2=self1.TextAddress2P.get('1.0', 'end-1c')
        tele=self1.TextTele1.get('1.0', 'end-1c')
        email=self1.TextEmail1.get('1.0', 'end-1c')
        try:
            query="INSERT INTO parents(Parents_FirstName,Parents_LastName,Parents_Address1,Parents_Address2,Parents_Telephone,Parents_Email)VALUES(%s,%s,%s,%s,?,%s)"
            val=(first,last,address1,address2,tele,email)
            cursor = mydb.cursor(prepared=True)
            cursor.execute(query,val)
            mydb.commit()
            JoinTh_c.showp(self,self1)
            messagebox.showinfo('adding successfully ','adding of parent info was successfully')
            self1.TextFirst1.delete('1.0', 'end')
            self1.TextLast1.delete('1.0', 'end')
            self1.TextAddress1P.delete('1.0', 'end')
            self1.TextAddress2P.delete('1.0', 'end')
            self1.TextTele1.delete('1.0', 'end')
            self1.TextEmail1.delete('1.0','end')
            JoinTh_c.helper(self,self1)
            
        except Exception:
            messagebox.showerror('Error in adding','Error in adding to the database')
      
    def deleParent(self,self1):
        p_id=self1.mysel2.get()
        try:
            q="DELETE FROM parents WHERE Parents_id= ?"
            val=p_id
            cursor = mydb.cursor(prepared=True)
            cursor.execute(q,(val,))
            mydb.commit()
            JoinTh_c.showp(self,self1)
            messagebox.showinfo('delete successfully ','delete of parent info was successfully')
            #self1.Text2.delete('1.0', 'end')
            self1.TCombobox2.set("")
            JoinTh_c.helper(self,self1)
        except Exception:
            messagebox.showerror('Error in deleting','Error in deleting of a record')

    def updateParent(self,self1):
        p_id=self1.Text1.get('1.0', 'end-1c')
        val=self1.mysel.get()
        try:
            if val=="first name":
                q="UPDATE parents SET Parents_FirstName  = %s WHERE Parents_id= ?"
                first=self1.TextFirst1.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextFirst1.delete('1.0', 'end')
                
                
            if val=="last name":
                q="UPDATE parents SET Parents_LastName  = %s WHERE Parents_id= ?"
                first=self1.TextLast1.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextLast1.delete('1.0', 'end')

            if val=="address1":
                q="UPDATE parents SET Parents_Address1  = %s WHERE Parents_id= ?"
                first=self1.TextAddress1P.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextAddress1P.delete('1.0', 'end')
                
            if val=="address2":
                q="UPDATE parents SET Parents_Address2  = %s WHERE Parents_id= ?"
                first=self1.TextAddress2P.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextAddress2P.delete('1.0', 'end')
                
            if val=="tele":
                q="UPDATE parents SET Parents_Telephone = ? WHERE Parents_id= ?"
                first=self1.TextTele1.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextTele1.delete('1.0', 'end')
                
            if val=="email":
                q="UPDATE parents SET Parents_Email  = %s WHERE Parents_id= ?"
                first=self1.TextEmail1.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showp(self,self1)
                messagebox.showinfo('update successfully ','update of parent info was successfully')
                self1.TextEmail1.delete(1.0,'end')
                
            self1.Text1.delete('1.0', 'end-1c')
            #self1.Text3.delete('1.0', 'end-1c')
            self1.TCombobox1.set("")
        except Exception:
            messagebox.showerror('Error in updating','Error in updating of a record')
#//////////////////////////////////CHILDREN CLASS FUNCTOIN/////////////////////////////////////////////////////////////////////////

    def helper2(self,self1):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Children_id FROM Children")
        myr=mycursor.fetchall()
        for x in myr:
            self1.TCombobox4['value']=(myr)
        self1.TCombobox4.set("")

    def showChild(self,self1):
        self1.Listbox1.delete(0,self1.Listbox1.size())
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from Children")
        rows = cursor.fetchall()
        
        for row in rows:
            self1.Listbox1.insert(1,row)

            
    def addChildren(self,self1):
        pid=self1.P_id.get('1.0', 'end-1c')
        first=self1.TextFirst2.get('1.0', 'end-1c')
        last=self1.TextLast2.get('1.0', 'end-1c')
        address1=self1.TextAddress1c.get('1.0', 'end-1c')
        address2=self1.TextAddress2c.get('1.0', 'end-1c')
        tele=self1.TextTele2.get('1.0', 'end-1c')
        try:
            query="INSERT INTO children(Parents_Id,Children_FirstName,Children_LastName,Children_DOB,Children_Attend,Children_sex)VALUES(?,%s,%s,%s,?,%s)"
            val=(pid,first,last,address1,address2,tele)
            cursor = mydb.cursor(prepared=True)
            cursor.execute(query,val)
            mydb.commit()
            JoinTh_c.showChild(self,self1)
            messagebox.showinfo('adding successfully ','adding of Chuldren info was successfully')
            self1.TextFirst2.delete('1.0', 'end')
            self1.TextLast2.delete('1.0', 'end')
            self1.TextAddress1c.delete('1.0', 'end')
            self1.TextAddress2c.delete('1.0', 'end')
            self1.TextTele2.delete('1.0', 'end')
            JoinTh_c.helper2(self,self1)
            
        except Exception:
            messagebox.showerror('Error in adding','Error in adding to th database')
             
            
    def deleChild(self,self1):
        p_id=self1.mysel4.get()
        try:
            q="DELETE FROM Children WHERE Children_id= ?"
            val=p_id
            cursor = mydb.cursor(prepared=True)
            cursor.execute(q,(val,))
            mydb.commit()
            JoinTh_c.showChild(self,self1)
            messagebox.showinfo('delete successfully ','delete of Children info was successfully')
            JoinTh_c.helper3(self,self1)
        except Exception:
            messagebox.showerror('Error in deleting','Error in deleting of a record')

            
    def updatechild(self,self1):
        p_id=self1.Text1.get('1.0', 'end-1c')
        val=self1.mysel3.get()
        try:
            if val=="first name":
                q="UPDATE Children SET Children_FirstName  = %s WHERE Children_id= ?"
                first=self1.TextFirst2.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showChild(self,self1)
                messagebox.showinfo('update successfully ','update of Children info was successfully')
                self1.TextFirst2.delete('1.0', 'end')
                
                
            if val=="last name":
                q="UPDATE Children SET Children_LastName  = %s WHERE Children_id= ?"
                first=self1.TextLast2.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showChild(self,self1)
                messagebox.showinfo('update successfully ','update of Chilren info was successfully')
                self1.TextLast2.delete('1.0', 'end')

            if val=="DOB":
                q="UPDATE Children SET Children_DOB  = %s WHERE Children_id= ?"
                first=self1.TextAddress1c.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showChild(self,self1)
                messagebox.showinfo('update successfully ','update of Children info was successfully')
                self1.TextAddress1c.delete('1.0', 'end')
                
            if val=="attend":
                q="UPDATE Children SET Children_Attend  = ? WHERE Children_id= ?"
                first=self1.TextAddress2c.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showChild(self,self1)
                messagebox.showinfo('update successfully ','update of Children info was successfully')
                self1.TextAddress2c.delete('1.0', 'end')
                
            if val=="sex":
                q="UPDATE Children SET Children_sex = %s WHERE Children_id= ?"
                first=self1.TextTele2.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showChild(self,self1)
                messagebox.showinfo('update successfully ','update ofChildren  info was successfully')
                self1.TextTele2.delete('1.0', 'end')
                
            self1.Text1.delete('1.0', 'end-1c')
            self1.TCombobox3.set("")
        except Exception:
            messagebox.showerror('Error in updating','Error in updating of a record')
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#*****************************WORKER CLASS*********************************************************************************
    def helper3(self,self1):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Employee_id FROM Worker")
        myr=mycursor.fetchall()
        for x in myr:
            self1.TCombobox4['value']=(myr)
        self1.TCombobox4.set("")

    def showWorker(self,self1):
        self1.Listbox1.delete(0,self1.Listbox1.size())
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from Worker")
        rows = cursor.fetchall()
        
        for row in rows:
            self1.Listbox1.insert(1,row)
            
    def deleWorker(self,self1):
        p_id=self1.mysel4.get()
        try:
            q="DELETE FROM Worker WHERE Employee_id= ?"
            val=p_id
            cursor = mydb.cursor(prepared=True)
            cursor.execute(q,(val,))
            mydb.commit()
            JoinTh_c.showWorker(self,self1)
            messagebox.showinfo('delete successfully ','delete of Worker info was successfully')
            JoinTh_c.helper3(self,self1)
        except Exception:
            messagebox.showerror('Error in deleting','Error in deleting of a record')

            
    def addWorker(self,self1):
        pid=self1.Text4.get('1.0', 'end-1c')
        first=self1.TextFirst3.get('1.0', 'end-1c')
        last=self1.TextLast3.get('1.0', 'end-1c')
        address1=self1.TextAddress1w.get('1.0', 'end-1c')
        address2=self1.TextAddress2w.get('1.0', 'end-1c')
        tele=self1.TextTele3.get('1.0', 'end-1c')
        email=self1.TextEmail3.get('1.0', 'end-1c')
        try:
            query="INSERT INTO Worker(Child_Id,Employee_FirstName,Employee_LastName,Employee_Address1,Employee_Address2,Employee_Telephone,Employee_Email)VALUES(?,%s,%s,%s,?,%s,%s)"
            val=(pid,first,last,address1,address2,tele,email)
            cursor = mydb.cursor(prepared=True)
            cursor.execute(query,val)
            mydb.commit()
            JoinTh_c.showWorker(self,self1)
            messagebox.showinfo('adding successfully ','adding of Worker info was successfully')
            self1.TextFirst3.delete('1.0', 'end')
            self1.TextLast3.delete('1.0', 'end')
            self1.TextAddress1w.delete('1.0', 'end')
            self1.TextAddress2w.delete('1.0', 'end')
            self1.TextTele3.delete('1.0', 'end')
            self1.TextEmail3.delete('1.0', 'end-1c')
            JoinTh_c.helper3(self,self1)
            
        except Exception:
            messagebox.showerror('Error in adding','Error in adding to th database')
            
    def updateWorker(self,self1):
        p_id=self1.Text1.get('1.0', 'end-1c')
        val=self1.mysel3.get()
        try:
            if val=="first name":
                q="UPDATE Worker SET Employee_FirstName  = %s WHERE Employee_id= ?"
                first=self1.TextFirst3.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextFirst3.delete('1.0', 'end')
                
                
            if val=="last name":
                q="UPDATE Worker SET Employee_LastName  = %s WHERE Employee_id= ?"
                first=self1.TextLast3.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextLast3.delete('1.0', 'end')

            if val=="address1":
                q="UPDATE Worker SET Employee_Address1  = %s WHERE Employee_id= ?"
                first=self1.TextAddress1w.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextAddress1w.delete('1.0', 'end')
                
            if val=="address2":
                q="UPDATE Worker SET Employee_Address2  = %s WHERE Employee_id= ?"
                first=self1.TextAddress2w.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextAddress2w.delete('1.0', 'end')
                
            if val=="tele":
                q="UPDATE Worker SET Employee_Telephone = ? WHERE Employee_id= ?"
                first=self1.TextTele3.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextTele3.delete('1.0', 'end')
                
            if val=="email":
                q="UPDATE Worker SET Employee_Email  = %s WHERE Employee_id= ?"
                first=self1.TextEmail3.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Worker info was successfully')
                self1.TextEmail3.delete(1.0,'end')
                
            self1.Text1.delete('1.0', 'end-1c')
            self1.TCombobox3.set("")
        except Exception:
            messagebox.showerror('Error in updating','Error in updating of a record')
#**************************************************************************************************************************

            
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def helper4(self,self1):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Event_id FROM Event")
        myr=mycursor.fetchall()
        for x in myr:
            self1.TCombobox4['value']=(myr)
        self1.TCombobox4.set("")

    def showEvent(self,self1):
        self1.Listbox1.delete(0,self1.Listbox1.size())
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from Event")
        rows = cursor.fetchall()
        
        for row in rows:
            self1.Listbox1.insert(1,row)
            
    def deleEvent(self,self1):
        p_id=self1.mysel4.get()
        try:
            q="DELETE FROM Event WHERE Event_id= ?"
            val=p_id
            cursor = mydb.cursor(prepared=True)
            cursor.execute(q,(val,))
            mydb.commit()
            JoinTh_c.showEvent(self,self1)
            messagebox.showinfo('delete successfully ','delete of Event info was successfully')
            JoinTh_c.helper4(self,self1)
        except Exception:
            messagebox.showerror('Error in deleting','Error in deleting of a record')
            
    def addEvent(self,self1):
        child=self1.Childtext.get('1.0', 'end-1c')
        worker=self1.workerText2.get('1.0', 'end-1c')
        name=self1.TextName.get('1.0', 'end-1c')
        time=self1.TextTime.get('1.0', 'end-1c')
        date=self1.TextDate.get('1.0', 'end-1c')
        cost=self1.Cost_Text1.get('1.0', 'end-1c')
        try:
            query="INSERT INTO Event(Child_id,Worker_id,Event_Name,Event_Time,Event_Date,Event_Cost)VALUES(?,?,%s,%s,%s,?)"
            val=(child,worker,name,time,date,cost)
            cursor = mydb.cursor(prepared=True)
            cursor.execute(query,val)
            mydb.commit()
            JoinTh_c.showEvent(self,self1)
            messagebox.showinfo('adding successfully ','adding of Event info was successfully')
            self1.Childtext.delete('1.0', 'end')
            self1.workerText2.delete('1.0', 'end')
            self1.TextName.delete('1.0', 'end')
            self1.TextTime.delete('1.0', 'end')
            self1.TextDate.delete('1.0', 'end')
            self1.Cost_Text1.delete('1.0', 'end')
            JoinTh_c.helper4(self,self1)
        except Exception:
            messagebox.showerror('Error in adding','Error in adding to th database')

    def updateEvent(self,self1):
        p_id=self1.Text1.get('1.0', 'end-1c')
        val=self1.mysel3.get()
        try:
            if val=="event name":
                q="UPDATE Event SET Event_Name  = %s WHERE Event_id= ?"
                first=self1.TextName.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showEvent(self,self1)
                messagebox.showinfo('update successfully ','update of Event info was successfully')
                self1.TextName.delete('1.0', 'end')
                
            if val=="event time":
                q="UPDATE Event SET Event_Time  = %s WHERE Event_id= ?"
                first=self1.TextTime.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showEvent(self,self1)
                messagebox.showinfo('update successfully ','update of Event info was successfully')
                self1.TextTime.delete('1.0', 'end')

            if val=="event date":
                q="UPDATE Event SET Event_Date  = %s WHERE Event_id= ?"
                first=self1.TextDate.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showWorker(self,self1)
                messagebox.showinfo('update successfully ','update of Event info was successfully')
                self1.TextDate.delete('1.0', 'end')
                
            self1.Text1.delete('1.0', 'end-1c')
            self1.TCombobox3.set("")
        except Exception:
            messagebox.showerror('Error in updating','Error in updating of a record')

    
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&




            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%SAVING CLASS FUNCTIONS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def helper5(self,self1):
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Saving_id FROM Saving")
        myr=mycursor.fetchall()
        for x in myr:
            self1.TCombobox4['value']=(myr)
        self1.TCombobox4.set("")

    def showSave(self,self1):
        self1.Listbox1.delete(0,self1.Listbox1.size())
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from Saving")
        rows = cursor.fetchall()
        
        for row in rows:
            self1.Listbox1.insert(1,row)
            
    def addSave(self,self1):
        first=self1.TextFirst.get('1.0', 'end-1c')
        last=self1.TextLast.get('1.0', 'end-1c')
        dep=self1.Saving_DText1.get('1.0', 'end-1c')

        cursor = mydb.cursor(prepared=True)
        q="select* from Event WHERE Event_id= ?"
        cursor.execute(q,(last,))
        rows = cursor.fetchall()
        val=rows[0][6]
        sum1=val-int(dep)
        try:
            query="INSERT INTO Saving(Child_id,Saving_Balance,Saving_Deposit)VALUES(?,?,?)"
            val=(first,sum1,dep)
            cursor = mydb.cursor(prepared=True)
            cursor.execute(query,val)
            mydb.commit()
            JoinTh_c.showSave(self,self1)
            messagebox.showinfo('adding successfully ','adding of Saving info was successfully')
            self1.TextFirst.delete('1.0', 'end')
            self1.TextLast.delete('1.0', 'end')
            JoinTh_c.helper5(self,self1)
        except Exception:
            messagebox.showerror('Error in adding','Error in adding to th database')
            
    def deleSave(self,self1):
        p_id=self1.mysel4.get()
        try:
            q="DELETE FROM Saving WHERE Saving_id= ?"
            val=p_id
            cursor = mydb.cursor(prepared=True)
            cursor.execute(q,(val,))
            mydb.commit()
            JoinTh_c.showSave(self,self1)
            messagebox.showinfo('delete successfully ','delete of Saving info was successfully')
            JoinTh_c.helper5(self,self1)
        except Exception:
            messagebox.showerror('Error in deleting','Error in deleting of a record')
    
            
    def updateSave(self,self1):
        p_id=self1.Text1.get('1.0', 'end-1c')
        val=self1.mysel3.get()
        try:
            if val=="saving":
                q="UPDATE Saving SET Saving_Deposit = ? WHERE Saving_id= ?"
                first=self1.Saving_DText1.get('1.0', 'end-1c')
                val2=(first,p_id)
                cursor = mydb.cursor(prepared=True)
                cursor.execute(q,val2)
                mydb.commit()
                JoinTh_c.showSave(self,self1)
                messagebox.showinfo('update successfully ','update of Saving info was successfully')
                self1.Saving_DText1.delete('1.0', 'end')
            self1.Text1.delete('1.0', 'end-1c')
            self1.TCombobox3.set("")
        except Exception:
            messagebox.showerror('Error in updating','Error in updating of a record')



            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    def sec(self,self1):
        val=self1.SearchText.get('1.0','end-1c')
        val2=self1.mysel5.get()
        val3=self1.mysel3.get()
        x=len(val)
        if val3=="parent" and x is 0:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("select * from parents")
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="parent" and val2=="first name":
            cursor = mydb.cursor(dictionary=True)
            q="select * from Parents WHERE Parents_FirstName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                    
        if val3=="parent" and val2=="last name" :
            cursor = mydb.cursor(dictionary=True)
            q="select * from Parents WHERE Parents_LastName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                    
        if val3=="parent" and val2=="Id":
            cursor = mydb.cursor(dictionary=True)
            q="select * FROM Parents WHERE Parents_id= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
                    
        if val3=="children" and x is 0:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("select * from Children")
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="children" and val2=="first name":
            cursor = mydb.cursor(dictionary=True)
            q="select * from Children WHERE Children_FirstName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="children" and val2=="last name" :
            cursor = mydb.cursor(dictionary=True)
            q="select * from Children WHERE Children_LastName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                    
        if val3=="children" and val2=="Id":
            cursor = mydb.cursor(dictionary=True)
            q="select * FROM Children WHERE Children_id= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="event" and x is 0:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("select * from Event")
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="event" and val2=="event name":
            cursor = mydb.cursor(dictionary=True)
            q="select * FROM Event WHERE Event_Name= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="event" and val2=="Id":
            cursor = mydb.cursor(dictionary=True)
            q="select * FROM Event WHERE Event_id= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="worker" and x is 0:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("select * from Worker")
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                
        if val3=="worker" and val2=="first name":
            cursor = mydb.cursor(dictionary=True)
            q="select * from Worker WHERE Employee_FirstName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                    
        if val3=="worker" and val2=="last name" :
            cursor = mydb.cursor(dictionary=True)
            q="select * from Worker WHERE Employee_LastName= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
                    
        if val3=="worker" and val2=="Id":
            cursor = mydb.cursor(dictionary=True)
            q="select * FROM Worker WHERE Employee_id= %s"
            cursor.execute(q,(val,))
            rows = cursor.fetchall()
            self1.Listbox1.delete(0,self1.Listbox1.size())
            for row in rows:
                self1.Listbox1.insert(1,row)
        self1.SearchText.delete('1.0', 'end-1c')
        self1.TCombobox1.set("")
        self1.TCombobox2.set("")



    def email(self,self1):
        new=2
        url="https://mail.yahoo.com"
        webbrowser.open(url,new=new)
                
    def attendReport(self,self1):
        mycursor=mydb.cursor(dictionary=True)
        mycursor.execute("SELECT Children_id,Children_Attend FROM Children")
        myr=mycursor.fetchall()
        x=canvas.Canvas("sample.pdf")
        c=""
        num=800
        for row in myr:
            c=str(row)
            x.drawString(50,num,c)
            num+=-25
          
        sum1=0
        for i in range(0,len(myr)):
            v=myr[i].values()
            n=list(v)[1]
            sum1=sum1+n
           
        total="Total attends :"+str(sum1)
        num-=25
        x.drawString(50,num,total)
        x.save()
        messagebox.showinfo('Report was successful','Report was printed')

    def assigment(self,self1):
          x=canvas.Canvas("sample1.pdf")
          mycursor=mydb.cursor(dictionary=True)
          mycursor.execute("SELECT Children_id,Children_FirstName,Children_LastName FROM Children")
          myr=mycursor.fetchall()
          print(myr)
          
          cursor = mydb.cursor(dictionary=True)
          cursor.execute("select Employee_FirstName,Employee_LastName  FROM Worker")
          rows = cursor.fetchall()
          print(rows)

    def login(self,self1):
        u=['adim','jevoy','mark']
        p=['123','icec00l']
        user=self1.Text1.get('1.0','end-1c')
        passwd=self1.Entry1.get()

        if user in u and passwd in p:
            JoinTh_c.show_frame(self,"Main")
            messagebox.showinfo('login successfully ','login was successfully')
        else:
            messagebox.showinfo('Wrong ','login was not successful')

           
        
        

#creating the login frame
class StartPage (tk.Frame):
        
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        top=self
        
        self.Frame1 = tk.Frame(self)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.place(relx=0.084, rely=0.04, relheight=0.277, relwidth=0.465)
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.157, rely=0.327, height=26, width=49)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''username''')
        
        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.067, rely=0.545, height=26, width=82)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''password''')
        self.Label2.configure(width=82)

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.315, rely=0.350, relheight=0.124, relwidth=0.346)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.21, rely=0.2,height=24, relwidth=0.24)
        self.Entry1.configure(background="white")
        self.Entry1.configure(show="*")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=144)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.36, rely=0.8, height=33, width=40)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=lambda:controller.login(self),text='''login''')
        top.configure(background="#d9d9d9")

         

        

       
       



# creatre the main funtoin of the system
class Main(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font13 = "-family {Arabic Transparent} -size 20 -weight normal"  \
            " -slant roman -underline 1 -overstrike 0"

        top=self


        self.Bt_Parent = tk.Button(self)
        self.Bt_Parent.place(relx=0.067, rely=0.578, height=33, width=54)
        self.Bt_Parent.configure(activebackground="#d9d9d9")
        self.Bt_Parent.configure(activeforeground="#000000")
        self.Bt_Parent.configure(background="#d9d9d9")
        self.Bt_Parent.configure(disabledforeground="#a3a3a3")
        self.Bt_Parent.configure(foreground="#000000")
        self.Bt_Parent.configure(highlightbackground="#d9d9d9")
        self.Bt_Parent.configure(highlightcolor="black")
        self.Bt_Parent.configure(pady="0")
        self.Bt_Parent.configure(command=lambda: controller.show_frame("parent"),text='''Parent''')

        self.BT_child = tk.Button(self)
        self.BT_child.place(relx=0.25, rely=0.578, height=33, width=67)
        self.BT_child.configure(activebackground="#d9d9d9")
        self.BT_child.configure(activeforeground="#000000")
        self.BT_child.configure(background="#d9d9d9")
        self.BT_child.configure(disabledforeground="#a3a3a3")
        self.BT_child.configure(foreground="#000000")
        self.BT_child.configure(highlightbackground="#d9d9d9")
        self.BT_child.configure(highlightcolor="black")
        self.BT_child.configure(pady="0")
        self.BT_child.configure(command=lambda: controller.show_frame("children"),text='''Children''')

        self.Bt_employ = tk.Button(self)
        self.Bt_employ.place(relx=0.417, rely=0.578, height=33, width=78)
        self.Bt_employ.configure(activebackground="#d9d9d9")
        self.Bt_employ.configure(activeforeground="#000000")
        self.Bt_employ.configure(background="#d9d9d9")
        self.Bt_employ.configure(disabledforeground="#a3a3a3")
        self.Bt_employ.configure(foreground="#000000")
        self.Bt_employ.configure(highlightbackground="#d9d9d9")
        self.Bt_employ.configure(highlightcolor="black")
        self.Bt_employ.configure(pady="0")
        self.Bt_employ.configure(command=lambda: controller.show_frame("worker"),text='''Worker''')

        self.Bt_event = tk.Button(self)
        self.Bt_event.place(relx=0.6, rely=0.578, height=33, width=54)
        self.Bt_event.configure(activebackground="#d9d9d9")
        self.Bt_event.configure(activeforeground="#000000")
        self.Bt_event.configure(background="#d9d9d9")
        self.Bt_event.configure(disabledforeground="#a3a3a3")
        self.Bt_event.configure(foreground="#000000")
        self.Bt_event.configure(highlightbackground="#d9d9d9")
        self.Bt_event.configure(highlightcolor="black")
        self.Bt_event.configure(pady="0")
        self.Bt_event.configure(command=lambda: controller.show_frame("event"),text='''Events''')

        self.Bt_save = tk.Button(self)
        self.Bt_save.place(relx=0.767, rely=0.578, height=33, width=60)
        self.Bt_save.configure(activebackground="#d9d9d9")
        self.Bt_save.configure(activeforeground="#000000")
        self.Bt_save.configure(background="#d9d9d9")
        self.Bt_save.configure(disabledforeground="#a3a3a3")
        self.Bt_save.configure(foreground="#000000")
        self.Bt_save.configure(highlightbackground="#d9d9d9")
        self.Bt_save.configure(highlightcolor="black")
        self.Bt_save.configure(pady="0")
        self.Bt_save.configure(command=lambda: controller.show_frame("saving"),text='''Saving''')

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.317, rely=0.022, height=56, width=182)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Main''')
        self.Label1.configure(width=182)

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.233, rely=0.2, height=116, width=292)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./download.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=292)

        self.Bt_search = tk.Button(self)
        self.Bt_search.place(relx=0.383, rely=0.733, height=33, width=54)
        self.Bt_search.configure(activebackground="#d9d9d9")
        self.Bt_search.configure(activeforeground="#000000")
        self.Bt_search.configure(background="#d9d9d9")
        self.Bt_search.configure(disabledforeground="#a3a3a3")
        self.Bt_search.configure(foreground="#000000")
        self.Bt_search.configure(highlightbackground="#d9d9d9")
        self.Bt_search.configure(highlightcolor="black")
        self.Bt_search.configure(pady="0")
        self.Bt_search.configure(command=lambda: controller.show_frame("search"),text='''search''')

        self.Bt_report = tk.Button(self)
        self.Bt_report.place(relx=0.55, rely=0.733, height=33, width=57)
        self.Bt_report.configure(activebackground="#d9d9d9")
        self.Bt_report.configure(activeforeground="#000000")
        self.Bt_report.configure(background="#d9d9d9")
        self.Bt_report.configure(disabledforeground="#a3a3a3")
        self.Bt_report.configure(foreground="#000000")
        self.Bt_report.configure(highlightbackground="#d9d9d9")
        self.Bt_report.configure(highlightcolor="black")
        self.Bt_report.configure(pady="0")
        self.Bt_report.configure(command=lambda: controller.show_frame("report"),text='''Report''')
        top.configure(background="#d9d9d9")



class parent(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font10 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font12 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"

        top=self
        
        self.controller.geometry("737x688+612+133")
        
        
        
        self.Parent_first = tk.Label(top)
        self.Parent_first.place(relx=0.027, rely=0.189, height=26, width=133)
        self.Parent_first.configure(activebackground="#f9f9f9")
        self.Parent_first.configure(activeforeground="black")
        self.Parent_first.configure(background="#d9d9d9")
        self.Parent_first.configure(disabledforeground="#a3a3a3")
        self.Parent_first.configure(font=font10)
        self.Parent_first.configure(foreground="#000000")
        self.Parent_first.configure(highlightbackground="#d9d9d9")
        self.Parent_first.configure(highlightcolor="black")
        self.Parent_first.configure(text='''Parent First Name''')

        self.parent_last = tk.Label(top)
        self.parent_last.place(relx=0.027, rely=0.262, height=26, width=131)
        self.parent_last.configure(activebackground="#f9f9f9")
        self.parent_last.configure(activeforeground="black")
        self.parent_last.configure(background="#d9d9d9")
        self.parent_last.configure(disabledforeground="#a3a3a3")
        self.parent_last.configure(font=font10)
        self.parent_last.configure(foreground="#000000")
        self.parent_last.configure(highlightbackground="#d9d9d9")
        self.parent_last.configure(highlightcolor="black")
        self.parent_last.configure(text='''Parent Last Name''')

        self.address1 = tk.Label(top)
        self.address1.place(relx=0.081, rely=0.334, height=26, width=72)
        self.address1.configure(activebackground="#f9f9f9")
        self.address1.configure(activeforeground="black")
        self.address1.configure(background="#d9d9d9")
        self.address1.configure(disabledforeground="#a3a3a3")
        self.address1.configure(font=font10)
        self.address1.configure(foreground="#000000")
        self.address1.configure(highlightbackground="#d9d9d9")
        self.address1.configure(highlightcolor="black")
        self.address1.configure(text='''Address1''')

        self.address2 = tk.Label(top)
        self.address2.place(relx=0.081, rely=0.407, height=26, width=72)
        self.address2.configure(activebackground="#f9f9f9")
        self.address2.configure(activeforeground="black")
        self.address2.configure(background="#d9d9d9")
        self.address2.configure(disabledforeground="#a3a3a3")
        self.address2.configure(font=font10)
        self.address2.configure(foreground="#000000")
        self.address2.configure(highlightbackground="#d9d9d9")
        self.address2.configure(highlightcolor="black")
        self.address2.configure(text='''Address2''')

        self.tele = tk.Label(top)
        self.tele.place(relx=0.081, rely=0.465, height=26, width=79)
        self.tele.configure(activebackground="#f9f9f9")
        self.tele.configure(activeforeground="black")
        self.tele.configure(background="#d9d9d9")
        self.tele.configure(disabledforeground="#a3a3a3")
        self.tele.configure(font=font10)
        self.tele.configure(foreground="#000000")
        self.tele.configure(highlightbackground="#d9d9d9")
        self.tele.configure(highlightcolor="black")
        self.tele.configure(text='''Telephone''')

        self.email = tk.Label(top)
        self.email.place(relx=0.122, rely=0.538, height=26, width=44)
        self.email.configure(activebackground="#f9f9f9")
        self.email.configure(activeforeground="black")
        self.email.configure(background="#d9d9d9")
        self.email.configure(disabledforeground="#a3a3a3")
        self.email.configure(font=font10)
        self.email.configure(foreground="#000000")
        self.email.configure(highlightbackground="#d9d9d9")
        self.email.configure(highlightcolor="black")
        self.email.configure(text='''Email''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.366, rely=0.015, height=46, width=142)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font12)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Parent''')

        self.TextFirst1 = tk.Text(top)
        self.TextFirst1.place(relx=0.217, rely=0.174, relheight=0.049
                , relwidth=0.236)
        self.TextFirst1.configure(background="white")
        self.TextFirst1.configure(font="TkTextFont")
        self.TextFirst1.configure(foreground="black")
        self.TextFirst1.configure(highlightbackground="#d9d9d9")
        self.TextFirst1.configure(highlightcolor="black")
        self.TextFirst1.configure(insertbackground="black")
        self.TextFirst1.configure(selectbackground="#c4c4c4")
        self.TextFirst1.configure(selectforeground="black")
        self.TextFirst1.configure(width=174)
        self.TextFirst1.configure(wrap='word')

        self.TextLast1 = tk.Text(top)
        self.TextLast1.place(relx=0.217, rely=0.247, relheight=0.049
                , relwidth=0.236)
        self.TextLast1.configure(background="white")
        self.TextLast1.configure(font="TkTextFont")
        self.TextLast1.configure(foreground="black")
        self.TextLast1.configure(highlightbackground="#d9d9d9")
        self.TextLast1.configure(highlightcolor="black")
        self.TextLast1.configure(insertbackground="black")
        self.TextLast1.configure(selectbackground="#c4c4c4")
        self.TextLast1.configure(selectforeground="black")
        self.TextLast1.configure(width=174)
        self.TextLast1.configure(wrap='word')

        self.TextAddress1P = tk.Text(top)
        self.TextAddress1P.place(relx=0.217, rely=0.32, relheight=0.049
                , relwidth=0.236)
        self.TextAddress1P.configure(background="white")
        self.TextAddress1P.configure(font="TkTextFont")
        self.TextAddress1P.configure(foreground="black")
        self.TextAddress1P.configure(highlightbackground="#d9d9d9")
        self.TextAddress1P.configure(highlightcolor="black")
        self.TextAddress1P.configure(insertbackground="black")
        self.TextAddress1P.configure(selectbackground="#c4c4c4")
        self.TextAddress1P.configure(selectforeground="black")
        self.TextAddress1P.configure(width=174)
        self.TextAddress1P.configure(wrap='word')

        self.TextAddress2P = tk.Text(top)
        self.TextAddress2P.place(relx=0.217, rely=0.392, relheight=0.049
                , relwidth=0.236)
        self.TextAddress2P.configure(background="white")
        self.TextAddress2P.configure(font="TkTextFont")
        self.TextAddress2P.configure(foreground="black")
        self.TextAddress2P.configure(highlightbackground="#d9d9d9")
        self.TextAddress2P.configure(highlightcolor="black")
        self.TextAddress2P.configure(insertbackground="black")
        self.TextAddress2P.configure(selectbackground="#c4c4c4")
        self.TextAddress2P.configure(selectforeground="black")
        self.TextAddress2P.configure(width=174)
        self.TextAddress2P.configure(wrap='word')

        self.TextTele1 = tk.Text(top)
        self.TextTele1.place(relx=0.217, rely=0.465, relheight=0.049
                , relwidth=0.236)
        self.TextTele1.configure(background="white")
        self.TextTele1.configure(font="TkTextFont")
        self.TextTele1.configure(foreground="black")
        self.TextTele1.configure(highlightbackground="#d9d9d9")
        self.TextTele1.configure(highlightcolor="black")
        self.TextTele1.configure(insertbackground="black")
        self.TextTele1.configure(selectbackground="#c4c4c4")
        self.TextTele1.configure(selectforeground="black")
        self.TextTele1.configure(width=174)
        self.TextTele1.configure(wrap='word')

        self.TextEmail1 = tk.Text(top)
        self.TextEmail1.place(relx=0.217, rely=0.538, relheight=0.049
                , relwidth=0.236)
        self.TextEmail1.configure(background="white")
        self.TextEmail1.configure(font="TkTextFont")
        self.TextEmail1.configure(foreground="black")
        self.TextEmail1.configure(highlightbackground="#d9d9d9")
        self.TextEmail1.configure(highlightcolor="black")
        self.TextEmail1.configure(insertbackground="black")
        self.TextEmail1.configure(selectbackground="#c4c4c4")
        self.TextEmail1.configure(selectforeground="black")
        self.TextEmail1.configure(width=174)
        self.TextEmail1.configure(wrap='word')

        n=self.Listbox0 = tk.Listbox(top)
        self.Listbox0.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.configure(background="white")
        self.Listbox0.configure(disabledforeground="#a3a3a3")
        self.Listbox0.configure(font="TkFixedFont")
        self.Listbox0.configure(foreground="#000000")
        self.Listbox0.configure(highlightbackground="#d9d9d9")
        self.Listbox0.configure(highlightcolor="black")
        self.Listbox0.configure(selectbackground="#c4c4c4")
        self.Listbox0.configure(selectforeground="black")
        self.Listbox0.configure(width=614)

        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox0.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox0.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')


        self.Pshow = tk.Button(top)
        self.Pshow.place(relx=0.19, rely=0.61, height=33, width=48)
        self.Pshow.configure(activebackground="#d9d9d9")
        self.Pshow.configure(activeforeground="#000000")
        self.Pshow.configure(background="#d9d9d9")
        self.Pshow.configure(disabledforeground="#a3a3a3")
        self.Pshow.configure(foreground="#000000")
        self.Pshow.configure(highlightbackground="#d9d9d9")
        self.Pshow.configure(highlightcolor="black")
        self.Pshow.configure(pady="0")
        self.Pshow.configure(command=lambda:controller.showp(self),text='''Show''')
        


        self.Pupdate = tk.Button(top)
        self.Pupdate.place(relx=0.76, rely=0.407, height=33, width=61)
        self.Pupdate.configure(activebackground="#d9d9d9")
        self.Pupdate.configure(activeforeground="#000000")
        self.Pupdate.configure(background="#d9d9d9")
        self.Pupdate.configure(disabledforeground="#a3a3a3")
        self.Pupdate.configure(foreground="#000000")
        self.Pupdate.configure(highlightbackground="#d9d9d9")
        self.Pupdate.configure(highlightcolor="black")
        self.Pupdate.configure(pady="0")
        self.Pupdate.configure(command=lambda:controller.updateParent(self),text='''Update''')

        self.P_add = tk.Button(top)
        self.P_add.place(relx=0.326, rely=0.61, height=33, width=40)
        self.P_add.configure(activebackground="#d9d9d9")
        self.P_add.configure(activeforeground="#000000")
        self.P_add.configure(background="#d9d9d9")
        self.P_add.configure(disabledforeground="#a3a3a3")
        self.P_add.configure(foreground="#000000")
        self.P_add.configure(highlightbackground="#d9d9d9")
        self.P_add.configure(highlightcolor="black")
        self.P_add.configure(pady="0")
        self.P_add.configure(command=lambda:controller.addParent(self),text='''Add''')

        self.Pdelete = tk.Button(top)
        self.Pdelete.place(relx=0.624, rely=0.509, height=33, width=56)
        self.Pdelete.configure(activebackground="#d9d9d9")
        self.Pdelete.configure(activeforeground="#000000")
        self.Pdelete.configure(background="#d9d9d9")
        self.Pdelete.configure(disabledforeground="#a3a3a3")
        self.Pdelete.configure(foreground="#000000")
        self.Pdelete.configure(highlightbackground="#d9d9d9")
        self.Pdelete.configure(highlightcolor="black")
        self.Pdelete.configure(pady="0")
        self.Pdelete.configure(command=lambda:controller.deleParent(self),text='''Delete''')

        self.eg1 = tk.Label(top)
        self.eg1.place(relx=0.488, rely=0.102, height=36, width=142)
        self.eg1.configure(activebackground="#f9f9f9")
        self.eg1.configure(activeforeground="black")
        self.eg1.configure(background="#d9d9d9")
        self.eg1.configure(disabledforeground="#a3a3a3")
        self.eg1.configure(foreground="#000000")
        self.eg1.configure(highlightbackground="#d9d9d9")
        self.eg1.configure(highlightcolor="black")
        self.eg1.configure(text='''Eg.ID: 11''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')


        self.labelDel = tk.Label(top)
        self.labelDel.place(relx=0.597, rely=0.451, height=26, width=89)
        self.labelDel.configure(background="#d9d9d9")
        self.labelDel.configure(disabledforeground="#a3a3a3")
        self.labelDel.configure(foreground="#000000")
        self.labelDel.configure(text='''Delete by ID''')

        self.LabelUpdate = tk.Label(top)
        self.LabelUpdate.place(relx=0.611, rely=0.305, height=26, width=72)
        self.LabelUpdate.configure(background="#d9d9d9")
        self.LabelUpdate.configure(disabledforeground="#a3a3a3")
        self.LabelUpdate.configure(foreground="#000000")
        self.LabelUpdate.configure(text='''Enter ID:''')
        self.LabelUpdate.configure(width=72)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.733, rely=0.291, relheight=0.049, relwidth=0.209)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word')

        self.TCombobox1 = ttk.Combobox(top)
        self.mysel=StringVar()
        self.TCombobox1['value']=("first name","last name","address1","address2","tele","email")
        self.TCombobox1.place(relx=0.719, rely=0.349, relheight=0.038
                , relwidth=0.254)
        self.TCombobox1.configure(textvariable=self.mysel)

        self.TCombobox1.configure(takefocus="")

        self.LabelNewU = tk.Label(top)
        self.LabelNewU.place(relx=0.529, rely=0.349, height=26, width=142)
        self.LabelNewU.configure(background="#d9d9d9")
        self.LabelNewU.configure(disabledforeground="#a3a3a3")
        self.LabelNewU.configure(foreground="#000000")
        self.LabelNewU.configure(text='''Update by:''')
        self.LabelNewU.configure(width=142)

        self.egupdate = tk.Label(top)
        self.egupdate.place(relx=0.773, rely=0.218, height=26, width=92)
        self.egupdate.configure(background="#d9d9d9")
        self.egupdate.configure(disabledforeground="#a3a3a3")
        self.egupdate.configure(foreground="#000000")
        self.egupdate.configure(text='''Eg: P_ID''')
        self.egupdate.configure(width=92)



        self.TCombobox2 = ttk.Combobox(top)
        self.mysel2=StringVar()
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Parents_id FROM Parents")
        myr=mycursor.fetchall()
        for x in myr:
            self.TCombobox2['value']=(myr)
        controller.helper(self)
        self.TCombobox2.place(relx=0.733, rely=0.509, relheight=0.049, relwidth=0.195)
        self.TCombobox2.configure(textvariable=self.mysel2)

        self.TCombobox2.configure(takefocus="")

        top.configure(background="#d9d9d9")

    


        

class children(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font10 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top=self
        
        self.Children_frist = tk.Label(top)
        self.Children_frist.place(relx=0.014, rely=0.189, height=26, width=155)
        self.Children_frist.configure(activebackground="#f9f9f9")
        self.Children_frist.configure(activeforeground="black")
        self.Children_frist.configure(background="#d9d9d9")
        self.Children_frist.configure(disabledforeground="#a3a3a3")
        self.Children_frist.configure(font=font9)
        self.Children_frist.configure(foreground="#000000")
        self.Children_frist.configure(highlightbackground="#d9d9d9")
        self.Children_frist.configure(highlightcolor="black")
        self.Children_frist.configure(text='''Children First Name''')
        self.Children_frist.configure(width=155)

        self.Children_last = tk.Label(top)
        self.Children_last.place(relx=0.014, rely=0.262, height=26, width=141)
        self.Children_last.configure(activebackground="#f9f9f9")
        self.Children_last.configure(activeforeground="black")
        self.Children_last.configure(background="#d9d9d9")
        self.Children_last.configure(disabledforeground="#a3a3a3")
        self.Children_last.configure(font=font9)
        self.Children_last.configure(foreground="#000000")
        self.Children_last.configure(highlightbackground="#d9d9d9")
        self.Children_last.configure(highlightcolor="black")
        self.Children_last.configure(text='''Children Last Name''')
        self.Children_last.configure(width=141)

        self.address1 = tk.Label(top)
        self.address1.place(relx=0.081, rely=0.334, height=26, width=72)
        self.address1.configure(activebackground="#f9f9f9")
        self.address1.configure(activeforeground="black")
        self.address1.configure(background="#d9d9d9")
        self.address1.configure(disabledforeground="#a3a3a3")
        self.address1.configure(font=font9)
        self.address1.configure(foreground="#000000")
        self.address1.configure(highlightbackground="#d9d9d9")
        self.address1.configure(highlightcolor="black")
        self.address1.configure(text='''Date Of Birth''')

        self.address2 = tk.Label(top)
        self.address2.place(relx=0.081, rely=0.407, height=26, width=72)
        self.address2.configure(activebackground="#f9f9f9")
        self.address2.configure(activeforeground="black")
        self.address2.configure(background="#d9d9d9")
        self.address2.configure(disabledforeground="#a3a3a3")
        self.address2.configure(font=font9)
        self.address2.configure(foreground="#000000")
        self.address2.configure(highlightbackground="#d9d9d9")
        self.address2.configure(highlightcolor="black")
        self.address2.configure(text='''Attend''')

        self.tele = tk.Label(top)
        self.tele.place(relx=0.081, rely=0.465, height=26, width=79)
        self.tele.configure(activebackground="#f9f9f9")
        self.tele.configure(activeforeground="black")
        self.tele.configure(background="#d9d9d9")
        self.tele.configure(disabledforeground="#a3a3a3")
        self.tele.configure(font=font9)
        self.tele.configure(foreground="#000000")
        self.tele.configure(highlightbackground="#d9d9d9")
        self.tele.configure(highlightcolor="black")
        self.tele.configure(text='''Sex''')


        self.Children = tk.Label(top)
        self.Children.place(relx=0.366, rely=0.015, height=46, width=142)
        self.Children.configure(activebackground="#f9f9f9")
        self.Children.configure(activeforeground="black")
        self.Children.configure(background="#d9d9d9")
        self.Children.configure(disabledforeground="#a3a3a3")
        self.Children.configure(font=font10)
        self.Children.configure(foreground="#000000")
        self.Children.configure(highlightbackground="#d9d9d9")
        self.Children.configure(highlightcolor="black")
        self.Children.configure(text='''Children''')

        self.TextFirst2 = tk.Text(top)
        self.TextFirst2.place(relx=0.217, rely=0.174, relheight=0.049
                , relwidth=0.236)
        self.TextFirst2.configure(background="white")
        self.TextFirst2.configure(font="TkTextFont")
        self.TextFirst2.configure(foreground="black")
        self.TextFirst2.configure(highlightbackground="#d9d9d9")
        self.TextFirst2.configure(highlightcolor="black")
        self.TextFirst2.configure(insertbackground="black")
        self.TextFirst2.configure(selectbackground="#c4c4c4")
        self.TextFirst2.configure(selectforeground="black")
        self.TextFirst2.configure(width=174)
        self.TextFirst2.configure(wrap='word')

        self.TextLast2= tk.Text(top)
        self.TextLast2.place(relx=0.217, rely=0.247, relheight=0.049
                , relwidth=0.236)
        self.TextLast2.configure(background="white")
        self.TextLast2.configure(font="TkTextFont")
        self.TextLast2.configure(foreground="black")
        self.TextLast2.configure(highlightbackground="#d9d9d9")
        self.TextLast2.configure(highlightcolor="black")
        self.TextLast2.configure(insertbackground="black")
        self.TextLast2.configure(selectbackground="#c4c4c4")
        self.TextLast2.configure(selectforeground="black")
        self.TextLast2.configure(width=174)
        self.TextLast2.configure(wrap='word')

        self.TextAddress1c = tk.Text(top)
        self.TextAddress1c.place(relx=0.217, rely=0.32, relheight=0.049
                , relwidth=0.236)
        self.TextAddress1c.configure(background="white")
        self.TextAddress1c.configure(font="TkTextFont")
        self.TextAddress1c.configure(foreground="black")
        self.TextAddress1c.configure(highlightbackground="#d9d9d9")
        self.TextAddress1c.configure(highlightcolor="black")
        self.TextAddress1c.configure(insertbackground="black")
        self.TextAddress1c.configure(selectbackground="#c4c4c4")
        self.TextAddress1c.configure(selectforeground="black")
        self.TextAddress1c.configure(width=174)
        self.TextAddress1c.configure(wrap='word')

        self.TextAddress2c = tk.Text(top)
        self.TextAddress2c.place(relx=0.217, rely=0.392, relheight=0.049
                , relwidth=0.236)
        self.TextAddress2c.configure(background="white")
        self.TextAddress2c.configure(font="TkTextFont")
        self.TextAddress2c.configure(foreground="black")
        self.TextAddress2c.configure(highlightbackground="#d9d9d9")
        self.TextAddress2c.configure(highlightcolor="black")
        self.TextAddress2c.configure(insertbackground="black")
        self.TextAddress2c.configure(selectbackground="#c4c4c4")
        self.TextAddress2c.configure(selectforeground="black")
        self.TextAddress2c.configure(width=174)
        self.TextAddress2c.configure(wrap='word')

        self.TextTele2 = tk.Text(top)
        self.TextTele2.place(relx=0.217, rely=0.465, relheight=0.049
                , relwidth=0.236)
        self.TextTele2.configure(background="white")
        self.TextTele2.configure(font="TkTextFont")
        self.TextTele2.configure(foreground="black")
        self.TextTele2.configure(highlightbackground="#d9d9d9")
        self.TextTele2.configure(highlightcolor="black")
        self.TextTele2.configure(insertbackground="black")
        self.TextTele2.configure(selectbackground="#c4c4c4")
        self.TextTele2.configure(selectforeground="black")
        self.TextTele2.configure(width=174)
        self.TextTele2.configure(wrap='word')

       

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=614)

        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox1.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox1.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')

        self.Pshow = tk.Button(top)
        self.Pshow.place(relx=0.19, rely=0.61, height=33, width=48)
        self.Pshow.configure(activebackground="#d9d9d9")
        self.Pshow.configure(activeforeground="#000000")
        self.Pshow.configure(background="#d9d9d9")
        self.Pshow.configure(disabledforeground="#a3a3a3")
        self.Pshow.configure(foreground="#000000")
        self.Pshow.configure(highlightbackground="#d9d9d9")
        self.Pshow.configure(highlightcolor="black")
        self.Pshow.configure(pady="0")
        self.Pshow.configure(command=lambda: controller.showChild(self),text='''Show''')

        self.Pupdate = tk.Button(top)
        self.Pupdate.place(relx=0.76, rely=0.407, height=33, width=61)
        self.Pupdate.configure(activebackground="#d9d9d9")
        self.Pupdate.configure(activeforeground="#000000")
        self.Pupdate.configure(background="#d9d9d9")
        self.Pupdate.configure(disabledforeground="#a3a3a3")
        self.Pupdate.configure(foreground="#000000")
        self.Pupdate.configure(highlightbackground="#d9d9d9")
        self.Pupdate.configure(highlightcolor="black")
        self.Pupdate.configure(pady="0")
        self.Pupdate.configure(command=lambda: controller.updatechild(self),text='''Update''')

        self.P_add = tk.Button(top)
        self.P_add.place(relx=0.326, rely=0.61, height=33, width=40)
        self.P_add.configure(activebackground="#d9d9d9")
        self.P_add.configure(activeforeground="#000000")
        self.P_add.configure(background="#d9d9d9")
        self.P_add.configure(disabledforeground="#a3a3a3")
        self.P_add.configure(foreground="#000000")
        self.P_add.configure(highlightbackground="#d9d9d9")
        self.P_add.configure(highlightcolor="black")
        self.P_add.configure(pady="0")
        self.P_add.configure(command=lambda: controller.addChildren(self),text='''Add''')

        self.Pdelete = tk.Button(top)
        self.Pdelete.place(relx=0.624, rely=0.509, height=33, width=56)
        self.Pdelete.configure(activebackground="#d9d9d9")
        self.Pdelete.configure(activeforeground="#000000")
        self.Pdelete.configure(background="#d9d9d9")
        self.Pdelete.configure(disabledforeground="#a3a3a3")
        self.Pdelete.configure(foreground="#000000")
        self.Pdelete.configure(highlightbackground="#d9d9d9")
        self.Pdelete.configure(highlightcolor="black")
        self.Pdelete.configure(pady="0")
        self.Pdelete.configure(command=lambda:controller.deleChild(self),text='''Delete''')

        self.eg1 = tk.Label(top)
        self.eg1.place(relx=0.488, rely=0.102, height=36, width=142)
        self.eg1.configure(activebackground="#f9f9f9")
        self.eg1.configure(activeforeground="black")
        self.eg1.configure(background="#d9d9d9")
        self.eg1.configure(disabledforeground="#a3a3a3")
        self.eg1.configure(foreground="#000000")
        self.eg1.configure(highlightbackground="#d9d9d9")
        self.eg1.configure(highlightcolor="black")
        self.eg1.configure(text='''Eg.ID: 11''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')

        self.labelDel = tk.Label(top)
        self.labelDel.place(relx=0.597, rely=0.451, height=26, width=89)
        self.labelDel.configure(background="#d9d9d9")
        self.labelDel.configure(disabledforeground="#a3a3a3")
        self.labelDel.configure(foreground="#000000")
        self.labelDel.configure(text='''Delete by ID''')

        self.LabelUpdate = tk.Label(top)
        self.LabelUpdate.place(relx=0.611, rely=0.305, height=26, width=72)
        self.LabelUpdate.configure(background="#d9d9d9")
        self.LabelUpdate.configure(disabledforeground="#a3a3a3")
        self.LabelUpdate.configure(foreground="#000000")
        self.LabelUpdate.configure(text='''Enter ID:''')
        self.LabelUpdate.configure(width=72)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.733, rely=0.291, relheight=0.049, relwidth=0.209)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word')

        self.TCombobox3 = ttk.Combobox(top)
        self.mysel3=StringVar()
        self.TCombobox3['value']=("first name","last name","DOB","attend","sex")
        self.TCombobox3.place(relx=0.719, rely=0.349, relheight=0.038
                , relwidth=0.254)
        self.TCombobox3.configure(textvariable=self.mysel3)

        self.TCombobox3.configure(takefocus="")

        self.LabelNewU = tk.Label(top)
        self.LabelNewU.place(relx=0.529, rely=0.349, height=26, width=142)
        self.LabelNewU.configure(background="#d9d9d9")
        self.LabelNewU.configure(disabledforeground="#a3a3a3")
        self.LabelNewU.configure(foreground="#000000")
        self.LabelNewU.configure(text='''Update by:''')
        self.LabelNewU.configure(width=142)

        self.egupdate = tk.Label(top)
        self.egupdate.place(relx=0.773, rely=0.218, height=26, width=92)
        self.egupdate.configure(background="#d9d9d9")
        self.egupdate.configure(disabledforeground="#a3a3a3")
        self.egupdate.configure(foreground="#000000")
        self.egupdate.configure(text='''Eg: P_ID''')
        self.egupdate.configure(width=92)

        self.TCombobox4 = ttk.Combobox(top)
        self.mysel4=StringVar()
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Children_id FROM Children")
        myr=mycursor.fetchall()
        for x in myr:
            self.TCombobox4['value']=(myr)
        controller.helper2(self)
        self.TCombobox4.place(relx=0.733, rely=0.509, relheight=0.049, relwidth=0.195)
        self.TCombobox4.configure(textvariable=self.mysel4)

        self.TCombobox4.configure(takefocus="")

        self.ParentID = tk.Label(top)
        self.ParentID.place(relx=0.054, rely=0.116, height=26, width=82)
        self.ParentID.configure(background="#d9d9d9")
        self.ParentID.configure(disabledforeground="#a3a3a3")
        self.ParentID.configure(font=font9)
        self.ParentID.configure(foreground="#000000")
        self.ParentID.configure(text='''ParentID''')
        self.ParentID.configure(width=82)

        self.P_id = tk.Text(top)
        self.P_id.place(relx=0.217, rely=0.116, relheight=0.049, relwidth=0.236)
        self.P_id.configure(background="white")
        self.P_id.configure(font="TkTextFont")
        self.P_id.configure(foreground="black")
        self.P_id.configure(highlightbackground="#d9d9d9")
        self.P_id.configure(highlightcolor="black")
        self.P_id.configure(insertbackground="black")
        self.P_id.configure(selectbackground="#c4c4c4")
        self.P_id.configure(selectforeground="black")
        self.P_id.configure(width=174)
        self.P_id.configure(wrap='word')

        top.configure(background="#d9d9d9") 

        

        
class worker(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font10 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top=self

        self.Worker_frist = tk.Label(top)
        self.Worker_frist.place(relx=0.014, rely=0.189, height=26, width=155)
        self.Worker_frist.configure(activebackground="#f9f9f9")
        self.Worker_frist.configure(activeforeground="black")
        self.Worker_frist.configure(background="#d9d9d9")
        self.Worker_frist.configure(disabledforeground="#a3a3a3")
        self.Worker_frist.configure(font=font9)
        self.Worker_frist.configure(foreground="#000000")
        self.Worker_frist.configure(highlightbackground="#d9d9d9")
        self.Worker_frist.configure(highlightcolor="black")
        self.Worker_frist.configure(text='''Worker First Name''')
        self.Worker_frist.configure(width=155)

        self.worker_last = tk.Label(top)
        self.worker_last.place(relx=0.014, rely=0.262, height=26, width=141)
        self.worker_last.configure(activebackground="#f9f9f9")
        self.worker_last.configure(activeforeground="black")
        self.worker_last.configure(background="#d9d9d9")
        self.worker_last.configure(disabledforeground="#a3a3a3")
        self.worker_last.configure(font=font9)
        self.worker_last.configure(foreground="#000000")
        self.worker_last.configure(highlightbackground="#d9d9d9")
        self.worker_last.configure(highlightcolor="black")
        self.worker_last.configure(text='''Worker Last Name''')
        self.worker_last.configure(width=141)

        self.address1 = tk.Label(top)
        self.address1.place(relx=0.081, rely=0.334, height=26, width=72)
        self.address1.configure(activebackground="#f9f9f9")
        self.address1.configure(activeforeground="black")
        self.address1.configure(background="#d9d9d9")
        self.address1.configure(disabledforeground="#a3a3a3")
        self.address1.configure(font=font9)
        self.address1.configure(foreground="#000000")
        self.address1.configure(highlightbackground="#d9d9d9")
        self.address1.configure(highlightcolor="black")
        self.address1.configure(text='''Address1''')

        self.address2 = tk.Label(top)
        self.address2.place(relx=0.081, rely=0.407, height=26, width=72)
        self.address2.configure(activebackground="#f9f9f9")
        self.address2.configure(activeforeground="black")
        self.address2.configure(background="#d9d9d9")
        self.address2.configure(disabledforeground="#a3a3a3")
        self.address2.configure(font=font9)
        self.address2.configure(foreground="#000000")
        self.address2.configure(highlightbackground="#d9d9d9")
        self.address2.configure(highlightcolor="black")
        self.address2.configure(text='''Address2''')

        self.tele = tk.Label(top)
        self.tele.place(relx=0.081, rely=0.465, height=26, width=79)
        self.tele.configure(activebackground="#f9f9f9")
        self.tele.configure(activeforeground="black")
        self.tele.configure(background="#d9d9d9")
        self.tele.configure(disabledforeground="#a3a3a3")
        self.tele.configure(font=font9)
        self.tele.configure(foreground="#000000")
        self.tele.configure(highlightbackground="#d9d9d9")
        self.tele.configure(highlightcolor="black")
        self.tele.configure(text='''Telephone''')

        self.email = tk.Label(top)
        self.email.place(relx=0.122, rely=0.538, height=26, width=44)
        self.email.configure(activebackground="#f9f9f9")
        self.email.configure(activeforeground="black")
        self.email.configure(background="#d9d9d9")
        self.email.configure(disabledforeground="#a3a3a3")
        self.email.configure(font=font9)
        self.email.configure(foreground="#000000")
        self.email.configure(highlightbackground="#d9d9d9")
        self.email.configure(highlightcolor="black")
        self.email.configure(text='''Email''')

        self.Worker = tk.Label(top)
        self.Worker.place(relx=0.366, rely=0.015, height=46, width=142)
        self.Worker.configure(activebackground="#f9f9f9")
        self.Worker.configure(activeforeground="black")
        self.Worker.configure(background="#d9d9d9")
        self.Worker.configure(disabledforeground="#a3a3a3")
        self.Worker.configure(font=font10)
        self.Worker.configure(foreground="#000000")
        self.Worker.configure(highlightbackground="#d9d9d9")
        self.Worker.configure(highlightcolor="black")
        self.Worker.configure(text='''Worker''')

        self.TextFirst3 = tk.Text(top)
        self.TextFirst3.place(relx=0.217, rely=0.174, relheight=0.049
                , relwidth=0.236)
        self.TextFirst3.configure(background="white")
        self.TextFirst3.configure(font="TkTextFont")
        self.TextFirst3.configure(foreground="black")
        self.TextFirst3.configure(highlightbackground="#d9d9d9")
        self.TextFirst3.configure(highlightcolor="black")
        self.TextFirst3.configure(insertbackground="black")
        self.TextFirst3.configure(selectbackground="#c4c4c4")
        self.TextFirst3.configure(selectforeground="black")
        self.TextFirst3.configure(width=174)
        self.TextFirst3.configure(wrap='word')

        self.TextLast3 = tk.Text(top)
        self.TextLast3.place(relx=0.217, rely=0.247, relheight=0.049
                , relwidth=0.236)
        self.TextLast3.configure(background="white")
        self.TextLast3.configure(font="TkTextFont")
        self.TextLast3.configure(foreground="black")
        self.TextLast3.configure(highlightbackground="#d9d9d9")
        self.TextLast3.configure(highlightcolor="black")
        self.TextLast3.configure(insertbackground="black")
        self.TextLast3.configure(selectbackground="#c4c4c4")
        self.TextLast3.configure(selectforeground="black")
        self.TextLast3.configure(width=174)
        self.TextLast3.configure(wrap='word')

        self.TextAddress1w = tk.Text(top)
        self.TextAddress1w.place(relx=0.217, rely=0.32, relheight=0.049
                , relwidth=0.236)
        self.TextAddress1w.configure(background="white")
        self.TextAddress1w.configure(font="TkTextFont")
        self.TextAddress1w.configure(foreground="black")
        self.TextAddress1w.configure(highlightbackground="#d9d9d9")
        self.TextAddress1w.configure(highlightcolor="black")
        self.TextAddress1w.configure(insertbackground="black")
        self.TextAddress1w.configure(selectbackground="#c4c4c4")
        self.TextAddress1w.configure(selectforeground="black")
        self.TextAddress1w.configure(width=174)
        self.TextAddress1w.configure(wrap='word')

        self.TextAddress2w = tk.Text(top)
        self.TextAddress2w.place(relx=0.217, rely=0.392, relheight=0.049
                , relwidth=0.236)
        self.TextAddress2w.configure(background="white")
        self.TextAddress2w.configure(font="TkTextFont")
        self.TextAddress2w.configure(foreground="black")
        self.TextAddress2w.configure(highlightbackground="#d9d9d9")
        self.TextAddress2w.configure(highlightcolor="black")
        self.TextAddress2w.configure(insertbackground="black")
        self.TextAddress2w.configure(selectbackground="#c4c4c4")
        self.TextAddress2w.configure(selectforeground="black")
        self.TextAddress2w.configure(width=174)
        self.TextAddress2w.configure(wrap='word')

        self.TextTele3 = tk.Text(top)
        self.TextTele3.place(relx=0.217, rely=0.465, relheight=0.049
                , relwidth=0.236)
        self.TextTele3.configure(background="white")
        self.TextTele3.configure(font="TkTextFont")
        self.TextTele3.configure(foreground="black")
        self.TextTele3.configure(highlightbackground="#d9d9d9")
        self.TextTele3.configure(highlightcolor="black")
        self.TextTele3.configure(insertbackground="black")
        self.TextTele3.configure(selectbackground="#c4c4c4")
        self.TextTele3.configure(selectforeground="black")
        self.TextTele3.configure(width=174)
        self.TextTele3.configure(wrap='word')

        self.TextEmail3 = tk.Text(top)
        self.TextEmail3.place(relx=0.217, rely=0.538, relheight=0.049
                , relwidth=0.236)
        self.TextEmail3.configure(background="white")
        self.TextEmail3.configure(font="TkTextFont")
        self.TextEmail3.configure(foreground="black")
        self.TextEmail3.configure(highlightbackground="#d9d9d9")
        self.TextEmail3.configure(highlightcolor="black")
        self.TextEmail3.configure(insertbackground="black")
        self.TextEmail3.configure(selectbackground="#c4c4c4")
        self.TextEmail3.configure(selectforeground="black")
        self.TextEmail3.configure(width=174)
        self.TextEmail3.configure(wrap='word')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=614)


        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox1.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox1.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')


        self.Pshow = tk.Button(top)
        self.Pshow.place(relx=0.19, rely=0.61, height=33, width=48)
        self.Pshow.configure(activebackground="#d9d9d9")
        self.Pshow.configure(activeforeground="#000000")
        self.Pshow.configure(background="#d9d9d9")
        self.Pshow.configure(disabledforeground="#a3a3a3")
        self.Pshow.configure(foreground="#000000")
        self.Pshow.configure(highlightbackground="#d9d9d9")
        self.Pshow.configure(highlightcolor="black")
        self.Pshow.configure(pady="0")
        self.Pshow.configure(command=lambda:controller.showWorker(self),text='''Show''')

        self.Pupdate = tk.Button(top)
        self.Pupdate.place(relx=0.76, rely=0.407, height=33, width=61)
        self.Pupdate.configure(activebackground="#d9d9d9")
        self.Pupdate.configure(activeforeground="#000000")
        self.Pupdate.configure(background="#d9d9d9")
        self.Pupdate.configure(disabledforeground="#a3a3a3")
        self.Pupdate.configure(foreground="#000000")
        self.Pupdate.configure(highlightbackground="#d9d9d9")
        self.Pupdate.configure(highlightcolor="black")
        self.Pupdate.configure(pady="0")
        self.Pupdate.configure(command=lambda:controller.updateWorker(self),text='''Update''')

        self.P_add = tk.Button(top)
        self.P_add.place(relx=0.326, rely=0.61, height=33, width=40)
        self.P_add.configure(activebackground="#d9d9d9")
        self.P_add.configure(activeforeground="#000000")
        self.P_add.configure(background="#d9d9d9")
        self.P_add.configure(disabledforeground="#a3a3a3")
        self.P_add.configure(foreground="#000000")
        self.P_add.configure(highlightbackground="#d9d9d9")
        self.P_add.configure(highlightcolor="black")
        self.P_add.configure(pady="0")
        self.P_add.configure(command=lambda:controller.addWorker(self),text='''Add''')

        self.Pdelete = tk.Button(top)
        self.Pdelete.place(relx=0.624, rely=0.509, height=33, width=56)
        self.Pdelete.configure(activebackground="#d9d9d9")
        self.Pdelete.configure(activeforeground="#000000")
        self.Pdelete.configure(background="#d9d9d9")
        self.Pdelete.configure(disabledforeground="#a3a3a3")
        self.Pdelete.configure(foreground="#000000")
        self.Pdelete.configure(highlightbackground="#d9d9d9")
        self.Pdelete.configure(highlightcolor="black")
        self.Pdelete.configure(pady="0")
        self.Pdelete.configure(command=lambda:controller.deleWorker(self),text='''Delete''')

        self.eg1 = tk.Label(top)
        self.eg1.place(relx=0.488, rely=0.102, height=36, width=142)
        self.eg1.configure(activebackground="#f9f9f9")
        self.eg1.configure(activeforeground="black")
        self.eg1.configure(background="#d9d9d9")
        self.eg1.configure(disabledforeground="#a3a3a3")
        self.eg1.configure(foreground="#000000")
        self.eg1.configure(highlightbackground="#d9d9d9")
        self.eg1.configure(highlightcolor="black")
        self.eg1.configure(text='''Eg.ID: 11''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')

        self.labelDel = tk.Label(top)
        self.labelDel.place(relx=0.597, rely=0.451, height=26, width=89)
        self.labelDel.configure(background="#d9d9d9")
        self.labelDel.configure(disabledforeground="#a3a3a3")
        self.labelDel.configure(foreground="#000000")
        self.labelDel.configure(text='''Delete by ID''')

        self.LabelUpdate = tk.Label(top)
        self.LabelUpdate.place(relx=0.611, rely=0.305, height=26, width=72)
        self.LabelUpdate.configure(background="#d9d9d9")
        self.LabelUpdate.configure(disabledforeground="#a3a3a3")
        self.LabelUpdate.configure(foreground="#000000")
        self.LabelUpdate.configure(text='''Enter ID:''')
        self.LabelUpdate.configure(width=72)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.733, rely=0.291, relheight=0.049, relwidth=0.209)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word') 


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.081, rely=0.131, height=26, width=82)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''Children_ID''')

        self.Text4 = tk.Text(top)
        self.Text4.place(relx=0.217, rely=0.131, relheight=0.035, relwidth=0.236)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=174)
        self.Text4.configure(wrap='word')

        self.LabelNewU = tk.Label(top)
        self.LabelNewU.place(relx=0.529, rely=0.349, height=26, width=142)
        self.LabelNewU.configure(background="#d9d9d9")
        self.LabelNewU.configure(disabledforeground="#a3a3a3")
        self.LabelNewU.configure(foreground="#000000")
        self.LabelNewU.configure(text='''Update by:''')
        self.LabelNewU.configure(width=142)

        self.egupdate = tk.Label(top)
        self.egupdate.place(relx=0.773, rely=0.218, height=26, width=92)
        self.egupdate.configure(background="#d9d9d9")
        self.egupdate.configure(disabledforeground="#a3a3a3")
        self.egupdate.configure(foreground="#000000")
        self.egupdate.configure(text='''Eg: P_ID''')
        self.egupdate.configure(width=92)

        self.TCombobox3 = ttk.Combobox(top)
        self.mysel3=StringVar()
        self.TCombobox3['value']=("first name","last name","address1","address2","tele","email")
        self.TCombobox3.place(relx=0.719, rely=0.349, relheight=0.038
                , relwidth=0.254)
        self.TCombobox3.configure(textvariable=self.mysel3)

        self.TCombobox3.configure(takefocus="")


        self.TCombobox4 = ttk.Combobox(top)
        self.mysel4=StringVar()
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Employee_id FROM Worker")
        myr=mycursor.fetchall()
        for x in myr:
            self.TCombobox4['value']=(myr)
        controller.helper3(self)
        self.TCombobox4.place(relx=0.733, rely=0.509, relheight=0.049, relwidth=0.195)
        self.TCombobox4.configure(textvariable=self.mysel4)

        self.TCombobox4.configure(takefocus="")
        top.configure(background="#d9d9d9")



        
class event(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font10 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"


        top=self

        self.event_frist = tk.Label(top)
        self.event_frist.place(relx=0.027, rely=0.247, height=26, width=155)
        self.event_frist.configure(activebackground="#f9f9f9")
        self.event_frist.configure(activeforeground="black")
        self.event_frist.configure(background="#d9d9d9")
        self.event_frist.configure(disabledforeground="#a3a3a3")
        self.event_frist.configure(font=font9)
        self.event_frist.configure(foreground="#000000")
        self.event_frist.configure(highlightbackground="#d9d9d9")
        self.event_frist.configure(highlightcolor="black")
        self.event_frist.configure(text='''Event Name''')
        self.event_frist.configure(width=155)

        self.event_last = tk.Label(top)
        self.event_last.place(relx=0.041, rely=0.305, height=26, width=141)
        self.event_last.configure(activebackground="#f9f9f9")
        self.event_last.configure(activeforeground="black")
        self.event_last.configure(background="#d9d9d9")
        self.event_last.configure(disabledforeground="#a3a3a3")
        self.event_last.configure(font=font9)
        self.event_last.configure(foreground="#000000")
        self.event_last.configure(highlightbackground="#d9d9d9")
        self.event_last.configure(highlightcolor="black")
        self.event_last.configure(text='''Event Time''')
        self.event_last.configure(width=141)

        self.address1 = tk.Label(top)
        self.address1.place(relx=0.068, rely=0.378, height=26, width=92)
        self.address1.configure(activebackground="#f9f9f9")
        self.address1.configure(activeforeground="black")
        self.address1.configure(background="#d9d9d9")
        self.address1.configure(disabledforeground="#a3a3a3")
        self.address1.configure(font=font9)
        self.address1.configure(foreground="#000000")
        self.address1.configure(highlightbackground="#d9d9d9")
        self.address1.configure(highlightcolor="black")
        self.address1.configure(text='''Event Date''')
        self.address1.configure(width=92)

        self.Event = tk.Label(top)
        self.Event.place(relx=0.366, rely=0.015, height=46, width=142)
        self.Event.configure(activebackground="#f9f9f9")
        self.Event.configure(activeforeground="black")
        self.Event.configure(background="#d9d9d9")
        self.Event.configure(disabledforeground="#a3a3a3")
        self.Event.configure(font=font10)
        self.Event.configure(foreground="#000000")
        self.Event.configure(highlightbackground="#d9d9d9")
        self.Event.configure(highlightcolor="black")
        self.Event.configure(text='''Event''')

        self.TextName = tk.Text(top)
        self.TextName.place(relx=0.217, rely=0.233, relheight=0.049
                , relwidth=0.236)
        self.TextName.configure(background="white")
        self.TextName.configure(font="TkTextFont")
        self.TextName.configure(foreground="black")
        self.TextName.configure(highlightbackground="#d9d9d9")
        self.TextName.configure(highlightcolor="black")
        self.TextName.configure(insertbackground="black")
        self.TextName.configure(selectbackground="#c4c4c4")
        self.TextName.configure(selectforeground="black")
        self.TextName.configure(width=174)
        self.TextName.configure(wrap='word')

        self.TextTime = tk.Text(top)
        self.TextTime.place(relx=0.217, rely=0.305, relheight=0.049
                , relwidth=0.236)
        self.TextTime.configure(background="white")
        self.TextTime.configure(font="TkTextFont")
        self.TextTime.configure(foreground="black")
        self.TextTime.configure(highlightbackground="#d9d9d9")
        self.TextTime.configure(highlightcolor="black")
        self.TextTime.configure(insertbackground="black")
        self.TextTime.configure(selectbackground="#c4c4c4")
        self.TextTime.configure(selectforeground="black")
        self.TextTime.configure(width=174)
        self.TextTime.configure(wrap='word')

        self.TextDate = tk.Text(top)
        self.TextDate.place(relx=0.217, rely=0.378, relheight=0.049
                , relwidth=0.236)
        self.TextDate.configure(background="white")
        self.TextDate.configure(font="TkTextFont")
        self.TextDate.configure(foreground="black")
        self.TextDate.configure(highlightbackground="#d9d9d9")
        self.TextDate.configure(highlightcolor="black")
        self.TextDate.configure(insertbackground="black")
        self.TextDate.configure(selectbackground="#c4c4c4")
        self.TextDate.configure(selectforeground="black")
        self.TextDate.configure(width=174)
        self.TextDate.configure(wrap='word')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=614)
      

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=614)


        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox1.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox1.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')

        self.eshow = tk.Button(top)
        self.eshow.place(relx=0.19, rely=0.61, height=33, width=48)
        self.eshow.configure(activebackground="#d9d9d9")
        self.eshow.configure(activeforeground="#000000")
        self.eshow.configure(background="#d9d9d9")
        self.eshow.configure(disabledforeground="#a3a3a3")
        self.eshow.configure(foreground="#000000")
        self.eshow.configure(highlightbackground="#d9d9d9")
        self.eshow.configure(highlightcolor="black")
        self.eshow.configure(pady="0")
        self.eshow.configure(command=lambda: controller.showEvent(self),text='''Show''')

        self.eupdate = tk.Button(top)
        self.eupdate.place(relx=0.76, rely=0.407, height=33, width=61)
        self.eupdate.configure(activebackground="#d9d9d9")
        self.eupdate.configure(activeforeground="#000000")
        self.eupdate.configure(background="#d9d9d9")
        self.eupdate.configure(disabledforeground="#a3a3a3")
        self.eupdate.configure(foreground="#000000")
        self.eupdate.configure(highlightbackground="#d9d9d9")
        self.eupdate.configure(highlightcolor="black")
        self.eupdate.configure(pady="0")
        self.eupdate.configure(command=lambda: controller.updateEvent(self),text='''Update''')

        self.e_add = tk.Button(top)
        self.e_add.place(relx=0.326, rely=0.61, height=33, width=40)
        self.e_add.configure(activebackground="#d9d9d9")
        self.e_add.configure(activeforeground="#000000")
        self.e_add.configure(background="#d9d9d9")
        self.e_add.configure(disabledforeground="#a3a3a3")
        self.e_add.configure(foreground="#000000")
        self.e_add.configure(highlightbackground="#d9d9d9")
        self.e_add.configure(highlightcolor="black")
        self.e_add.configure(pady="0")
        self.e_add.configure(command=lambda: controller.addEvent(self),text='''Add''')

        self.Edelete = tk.Button(top)
        self.Edelete.place(relx=0.624, rely=0.509, height=33, width=56)
        self.Edelete.configure(activebackground="#d9d9d9")
        self.Edelete.configure(activeforeground="#000000")
        self.Edelete.configure(background="#d9d9d9")
        self.Edelete.configure(disabledforeground="#a3a3a3")
        self.Edelete.configure(foreground="#000000")
        self.Edelete.configure(highlightbackground="#d9d9d9")
        self.Edelete.configure(highlightcolor="black")
        self.Edelete.configure(pady="0")
        self.Edelete.configure(command=lambda: controller.deleEvent(self),text='''Delete''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')

        self.worker_Id = tk.Label(top)
        self.worker_Id.place(relx=0.081, rely=0.189, height=29, width=89)
        self.worker_Id.configure(background="#d9d9d9")
        self.worker_Id.configure(disabledforeground="#a3a3a3")
        self.worker_Id.configure(font=font12)
        self.worker_Id.configure(foreground="#000000")
        self.worker_Id.configure(text='''Worker ID''')

        self.Child_ID = tk.Label(top)
        self.Child_ID.place(relx=0.095, rely=0.131, height=26, width=61)
        self.Child_ID.configure(background="#d9d9d9")
        self.Child_ID.configure(disabledforeground="#a3a3a3")
        self.Child_ID.configure(font=font12)
        self.Child_ID.configure(foreground="#000000")
        self.Child_ID.configure(text='''Child ID''')

        self.Childtext = tk.Text(top)
        self.Childtext.place(relx=0.217, rely=0.116, relheight=0.049
                , relwidth=0.236)
        self.Childtext.configure(background="white")
        self.Childtext.configure(font="TkTextFont")
        self.Childtext.configure(foreground="black")
        self.Childtext.configure(highlightbackground="#d9d9d9")
        self.Childtext.configure(highlightcolor="black")
        self.Childtext.configure(insertbackground="black")
        self.Childtext.configure(selectbackground="#c4c4c4")
        self.Childtext.configure(selectforeground="black")
        self.Childtext.configure(width=174)
        self.Childtext.configure(wrap='word')

        self.workerText2 = tk.Text(top)
        self.workerText2.place(relx=0.217, rely=0.174, relheight=0.049
                , relwidth=0.236)
        self.workerText2.configure(background="white")
        self.workerText2.configure(font="TkTextFont")
        self.workerText2.configure(foreground="black")
        self.workerText2.configure(highlightbackground="#d9d9d9")
        self.workerText2.configure(highlightcolor="black")
        self.workerText2.configure(insertbackground="black")
        self.workerText2.configure(selectbackground="#c4c4c4")
        self.workerText2.configure(selectforeground="black")
        self.workerText2.configure(width=174)
        self.workerText2.configure(wrap='word')

        self.labelDel = tk.Label(top)
        self.labelDel.place(relx=0.597, rely=0.451, height=26, width=89)
        self.labelDel.configure(background="#d9d9d9")
        self.labelDel.configure(disabledforeground="#a3a3a3")
        self.labelDel.configure(foreground="#000000")
        self.labelDel.configure(text='''Delete by ID''')

        self.LabelUpdate = tk.Label(top)
        self.LabelUpdate.place(relx=0.611, rely=0.305, height=26, width=90)
        self.LabelUpdate.configure(background="#d9d9d9")
        self.LabelUpdate.configure(disabledforeground="#a3a3a3")
        self.LabelUpdate.configure(foreground="#000000")
        self.LabelUpdate.configure(text='''Enter ID:''')
        self.LabelUpdate.configure(width=72)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.733, rely=0.291, relheight=0.049, relwidth=0.209)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word')



        self.LabelNewU = tk.Label(top)
        self.LabelNewU.place(relx=0.529, rely=0.349, height=26, width=142)
        self.LabelNewU.configure(background="#d9d9d9")
        self.LabelNewU.configure(disabledforeground="#a3a3a3")
        self.LabelNewU.configure(foreground="#000000")
        self.LabelNewU.configure(text='''Update by:''')
        self.LabelNewU.configure(width=142)

        self.egupdate = tk.Label(top)
        self.egupdate.place(relx=0.773, rely=0.218, height=26, width=92)
        self.egupdate.configure(background="#d9d9d9")
        self.egupdate.configure(disabledforeground="#a3a3a3")
        self.egupdate.configure(foreground="#000000")
        self.egupdate.configure(text='''Eg: P_ID''')
        self.egupdate.configure(width=92)


        self.TCombobox3 = ttk.Combobox(top)
        self.mysel3=StringVar()
        self.TCombobox3['value']=("event name","event time","event date")
        self.TCombobox3.place(relx=0.719, rely=0.349, relheight=0.038
                , relwidth=0.254)
        self.TCombobox3.configure(textvariable=self.mysel3)

        self.TCombobox3.configure(takefocus="")


        self.TCombobox4 = ttk.Combobox(top)
        self.mysel4=StringVar()
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Event_id FROM Event")
        myr=mycursor.fetchall()
        for x in myr:
            self.TCombobox4['value']=(myr)
        controller.helper4(self)
        self.TCombobox4.place(relx=0.733, rely=0.509, relheight=0.049, relwidth=0.195)
        self.TCombobox4.configure(textvariable=self.mysel4)

        self.TCombobox4.configure(takefocus="")

        self.TCombobox4.configure(takefocus="")
        self.Cost_Label = tk.Label(top)
        self.Cost_Label.place(relx=0.081, rely=0.436, height=26, width=80)
        self.Cost_Label.configure(background="#d9d9d9")
        self.Cost_Label.configure(disabledforeground="#a3a3a3")
        self.Cost_Label.configure(font=font9)
        self.Cost_Label.configure(foreground="#000000")
        self.Cost_Label.configure(text='''Event Cost''')

        self.Cost_Text1 = tk.Text(top)
        self.Cost_Text1.place(relx=0.217, rely=0.436, relheight=0.049
                , relwidth=0.236)
        self.Cost_Text1.configure(background="white")
        self.Cost_Text1.configure(font="TkTextFont")
        self.Cost_Text1.configure(foreground="black")
        self.Cost_Text1.configure(highlightbackground="#d9d9d9")
        self.Cost_Text1.configure(highlightcolor="black")
        self.Cost_Text1.configure(insertbackground="black")
        self.Cost_Text1.configure(selectbackground="#c4c4c4")
        self.Cost_Text1.configure(selectforeground="black")
        self.Cost_Text1.configure(width=174)
        self.Cost_Text1.configure(wrap='word')
        top.configure(background="#d9d9d9")





        
        
class saving(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        font10 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top=self

        self.save_frist = tk.Label(top)
        self.save_frist.place(relx=0.014, rely=0.262, height=26, width=155)
        self.save_frist.configure(activebackground="#f9f9f9")
        self.save_frist.configure(activeforeground="black")
        self.save_frist.configure(background="#d9d9d9")
        self.save_frist.configure(disabledforeground="#a3a3a3")
        self.save_frist.configure(font=font9)
        self.save_frist.configure(foreground="#000000")
        self.save_frist.configure(highlightbackground="#d9d9d9")
        self.save_frist.configure(highlightcolor="black")
        self.save_frist.configure(text='''Child ID''')
        self.save_frist.configure(width=155)

        self.Account = tk.Label(top)
        self.Account.place(relx=0.027, rely=0.349, height=26, width=141)
        self.Account.configure(activebackground="#f9f9f9")
        self.Account.configure(activeforeground="black")
        self.Account.configure(background="#d9d9d9")
        self.Account.configure(disabledforeground="#a3a3a3")
        self.Account.configure(font=font9)
        self.Account.configure(foreground="#000000")
        self.Account.configure(highlightbackground="#d9d9d9")
        self.Account.configure(highlightcolor="black")
        self.Account.configure(text='''Event ID''')
        self.Account.configure(width=141)

        self.Save = tk.Label(top)
        self.Save.place(relx=0.366, rely=0.015, height=46, width=142)
        self.Save.configure(activebackground="#f9f9f9")
        self.Save.configure(activeforeground="black")
        self.Save.configure(background="#d9d9d9")
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(font=font10)
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#d9d9d9")
        self.Save.configure(highlightcolor="black")
        self.Save.configure(text='''Save''')

        self.TextFirst = tk.Text(top)
        self.TextFirst.place(relx=0.217, rely=0.247, relheight=0.049
                , relwidth=0.236)
        self.TextFirst.configure(background="white")
        self.TextFirst.configure(font="TkTextFont")
        self.TextFirst.configure(foreground="black")
        self.TextFirst.configure(highlightbackground="#d9d9d9")
        self.TextFirst.configure(highlightcolor="black")
        self.TextFirst.configure(insertbackground="black")
        self.TextFirst.configure(selectbackground="#c4c4c4")
        self.TextFirst.configure(selectforeground="black")
        self.TextFirst.configure(width=174)
        self.TextFirst.configure(wrap='word')

        self.TextLast = tk.Text(top)
        self.TextLast.place(relx=0.217, rely=0.349, relheight=0.049
                , relwidth=0.236)
        self.TextLast.configure(background="white")
        self.TextLast.configure(font="TkTextFont")
        self.TextLast.configure(foreground="black")
        self.TextLast.configure(highlightbackground="#d9d9d9")
        self.TextLast.configure(highlightcolor="black")
        self.TextLast.configure(insertbackground="black")
        self.TextLast.configure(selectbackground="#c4c4c4")
        self.TextLast.configure(selectforeground="black")
        self.TextLast.configure(width=174)
        self.TextLast.configure(wrap='word')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.095, rely=0.683, relheight=0.288
                , relwidth=0.833)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=614)

        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox1.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox1.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')


        self.Pshow = tk.Button(top)
        self.Pshow.place(relx=0.19, rely=0.61, height=33, width=48)
        self.Pshow.configure(activebackground="#d9d9d9")
        self.Pshow.configure(activeforeground="#000000")
        self.Pshow.configure(background="#d9d9d9")
        self.Pshow.configure(disabledforeground="#a3a3a3")
        self.Pshow.configure(foreground="#000000")
        self.Pshow.configure(highlightbackground="#d9d9d9")
        self.Pshow.configure(highlightcolor="black")
        self.Pshow.configure(pady="0")
        self.Pshow.configure(command=lambda: controller.showSave(self),text='''Show''')

        self.Pupdate = tk.Button(top)
        self.Pupdate.place(relx=0.76, rely=0.407, height=33, width=61)
        self.Pupdate.configure(activebackground="#d9d9d9")
        self.Pupdate.configure(activeforeground="#000000")
        self.Pupdate.configure(background="#d9d9d9")
        self.Pupdate.configure(disabledforeground="#a3a3a3")
        self.Pupdate.configure(foreground="#000000")
        self.Pupdate.configure(highlightbackground="#d9d9d9")
        self.Pupdate.configure(highlightcolor="black")
        self.Pupdate.configure(pady="0")
        self.Pupdate.configure(command=lambda: controller.updateSave(self),text='''Update''')

        self.P_add = tk.Button(top)
        self.P_add.place(relx=0.326, rely=0.61, height=33, width=40)
        self.P_add.configure(activebackground="#d9d9d9")
        self.P_add.configure(activeforeground="#000000")
        self.P_add.configure(background="#d9d9d9")
        self.P_add.configure(disabledforeground="#a3a3a3")
        self.P_add.configure(foreground="#000000")
        self.P_add.configure(highlightbackground="#d9d9d9")
        self.P_add.configure(highlightcolor="black")
        self.P_add.configure(pady="0")
        self.P_add.configure(command=lambda: controller.addSave(self),text='''Add''')

        self.Pdelete = tk.Button(top)
        self.Pdelete.place(relx=0.624, rely=0.509, height=33, width=56)
        self.Pdelete.configure(activebackground="#d9d9d9")
        self.Pdelete.configure(activeforeground="#000000")
        self.Pdelete.configure(background="#d9d9d9")
        self.Pdelete.configure(disabledforeground="#a3a3a3")
        self.Pdelete.configure(foreground="#000000")
        self.Pdelete.configure(highlightbackground="#d9d9d9")
        self.Pdelete.configure(highlightcolor="black")
        self.Pdelete.configure(pady="0")
        self.Pdelete.configure(command=lambda: controller.deleSave(self),text='''Delete''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')

        self.labelDel = tk.Label(top)
        self.labelDel.place(relx=0.597, rely=0.451, height=26, width=89)
        self.labelDel.configure(background="#d9d9d9")
        self.labelDel.configure(disabledforeground="#a3a3a3")
        self.labelDel.configure(foreground="#000000")
        self.labelDel.configure(text='''Delete by ID''')

        self.LabelUpdate = tk.Label(top)
        self.LabelUpdate.place(relx=0.611, rely=0.305, height=26, width=72)
        self.LabelUpdate.configure(background="#d9d9d9")
        self.LabelUpdate.configure(disabledforeground="#a3a3a3")
        self.LabelUpdate.configure(foreground="#000000")
        self.LabelUpdate.configure(text='''Enter ID:''')
        self.LabelUpdate.configure(width=72)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.733, rely=0.291, relheight=0.049, relwidth=0.209)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=154)
        self.Text1.configure(wrap='word')


        self.LabelNewU = tk.Label(top)
        self.LabelNewU.place(relx=0.529, rely=0.349, height=26, width=142)
        self.LabelNewU.configure(background="#d9d9d9")
        self.LabelNewU.configure(disabledforeground="#a3a3a3")
        self.LabelNewU.configure(foreground="#000000")
        self.LabelNewU.configure(text='''Update by:''')
        self.LabelNewU.configure(width=142)

        self.egupdate = tk.Label(top)
        self.egupdate.place(relx=0.773, rely=0.218, height=26, width=92)
        self.egupdate.configure(background="#d9d9d9")
        self.egupdate.configure(disabledforeground="#a3a3a3")
        self.egupdate.configure(foreground="#000000")
        self.egupdate.configure(text='''Eg: P_ID''')
        self.egupdate.configure(width=92)

        self.TCombobox3 = ttk.Combobox(top)
        self.mysel3=StringVar()
        self.TCombobox3['value']=("saving")
        self.TCombobox3.place(relx=0.719, rely=0.349, relheight=0.038
                , relwidth=0.254)
        self.TCombobox3.configure(textvariable=self.mysel3)

        self.TCombobox3.configure(takefocus="")


        self.TCombobox4 = ttk.Combobox(top)
        self.mysel4=StringVar()
        mycursor=mydb.cursor()
        mycursor.execute("SELECT Saving_id FROM Saving")
        myr=mycursor.fetchall()
        for x in myr:
            self.TCombobox4['value']=(myr)
        controller.helper5(self)
        self.TCombobox4.place(relx=0.733, rely=0.509, relheight=0.049, relwidth=0.195)
        self.TCombobox4.configure(textvariable=self.mysel4)

        self.Saving_DLabel1 = tk.Label(top)
        self.Saving_DLabel1.place(relx=0.043, rely=0.420, height=26, width=110)
        self.Saving_DLabel1.configure(background="#d9d9d9")
        self.Saving_DLabel1.configure(disabledforeground="#a3a3a3")
        self.Saving_DLabel1.configure(font=font9)
        self.Saving_DLabel1.configure(foreground="#000000")
        self.Saving_DLabel1.configure(text='''Saving Deposit''')

        self.Saving_DText1 = tk.Text(top)
        self.Saving_DText1.place(relx=0.220, rely=0.420, relheight=0.046
                , relwidth=0.24)
        self.Saving_DText1.configure(background="white")
        self.Saving_DText1.configure(font="TkTextFont")
        self.Saving_DText1.configure(foreground="black")
        self.Saving_DText1.configure(highlightbackground="#d9d9d9")
        self.Saving_DText1.configure(highlightcolor="black")
        self.Saving_DText1.configure(insertbackground="black")
        self.Saving_DText1.configure(selectbackground="#c4c4c4")
        self.Saving_DText1.configure(selectforeground="black")
        self.Saving_DText1.configure(width=144)
        self.Saving_DText1.configure(wrap='word')

        


        
        top.configure(background="#d9d9d9")
        
	
	
	
class search(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        top=self
        top.configure(background="#d9d9d9")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.033, rely=0.511, relheight=0.462 , relwidth=0.94)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=454)

        scrollbar = Scrollbar(self, orient="horizontal")
        scrollbar.config(command= self.Listbox1.xview)
        scrollbar.pack(side="bottom", fill="x")

        self.Listbox1.config(xscrollcommand=scrollbar.set)
        scrollbar.set('0', '0.1')

        self.searchBy = tk.Label(top)
        self.searchBy.place(relx=0.067, rely=0.267, height=26, width=74)
        self.searchBy.configure(background="#d9d9d9")
        self.searchBy.configure(disabledforeground="#a3a3a3")
        self.searchBy.configure(foreground="#000000")
        self.searchBy.configure(text='''Search by''')

        self.EnterLabel = tk.Label(top)
        self.EnterLabel.place(relx=0.067, rely=0.156, height=26, width=59)
        self.EnterLabel.configure(background="#d9d9d9")
        self.EnterLabel.configure(disabledforeground="#a3a3a3")
        self.EnterLabel.configure(foreground="#000000")
        self.EnterLabel.configure(text='''Enter value''')

        self.SearchText = tk.Text(top)
        self.SearchText.place(relx=0.217, rely=0.156, relheight=0.076
                , relwidth=0.307)
        self.SearchText.configure(background="white")
        self.SearchText.configure(font="TkTextFont")
        self.SearchText.configure(foreground="black")
        self.SearchText.configure(highlightbackground="#d9d9d9")
        self.SearchText.configure(highlightcolor="black")
        self.SearchText.configure(insertbackground="black")
        self.SearchText.configure(selectbackground="#c4c4c4")
        self.SearchText.configure(selectforeground="black")
        self.SearchText.configure(width=184)
        self.SearchText.configure(wrap='word')

        self.categoryText = tk.Label(top)
        self.categoryText.place(relx=0.033, rely=0.067, height=26, width=102)
        self.categoryText.configure(background="#d9d9d9")
        self.categoryText.configure(disabledforeground="#a3a3a3")
        self.categoryText.configure(foreground="#000000")
        self.categoryText.configure(text='''Category''')
        self.categoryText.configure(width=102)
        

        self.TCombobox1 = ttk.Combobox(top)
        self.mysel3=StringVar()
        self.TCombobox1['value']=("parent","children","worker","event")
        self.TCombobox1.place(relx=0.217, rely=0.267, relheight=0.058
                , relwidth=0.312)
        self.TCombobox1.configure(textvariable=self.mysel3)
        self.TCombobox1.configure(takefocus="")
      
      
        self.TCombobox2 = ttk.Combobox(top)
        self.mysel5=StringVar()
        self.TCombobox2['value']=("Id","first name","last name","event name","gender")
        self.TCombobox2.place(relx=0.217, rely=0.067, relheight=0.058
            , relwidth=0.312)
        self.TCombobox2.configure(textvariable=self.mysel5)
        self.TCombobox2.configure(takefocus="")

        self.S_Button1 = tk.Button(top)
        self.S_Button1.place(relx=0.283, rely=0.378, height=33, width=56)
        self.S_Button1.configure(activebackground="#d9d9d9")
        self.S_Button1.configure(activeforeground="#000000")
        self.S_Button1.configure(background="#d9d9d9")
        self.S_Button1.configure(disabledforeground="#a3a3a3")
        self.S_Button1.configure(foreground="#000000")
        self.S_Button1.configure(highlightbackground="#d9d9d9")
        self.S_Button1.configure(highlightcolor="black")
        self.S_Button1.configure(pady="0")
        self.S_Button1.configure(command=lambda: controller.sec(self),text='''Search''')

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')

       
class report(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        font10 = "-family Arial -size 12 -weight bold -slant roman "  \
            "-underline 1 -overstrike 0"

        top=self
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.133, rely=0.111, relheight=0.611
                , relwidth=0.708)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=425)

        self.ReportButton = tk.Button(self.Frame1)
        self.ReportButton.place(relx=0.118, rely=0.109, height=33, width=91)
        self.ReportButton.configure(activebackground="#d9d9d9")
        self.ReportButton.configure(activeforeground="#000000")
        self.ReportButton.configure(background="#d9d9d9")
        self.ReportButton.configure(disabledforeground="#a3a3a3")
        self.ReportButton.configure(foreground="#000000")
        self.ReportButton.configure(highlightbackground="#d9d9d9")
        self.ReportButton.configure(highlightcolor="black")
        self.ReportButton.configure(pady="0")
        self.ReportButton.configure(command=lambda: controller.attendReport(self),text='''Print Report''')

        self.emailButton = tk.Button(self.Frame1)
        self.emailButton.place(relx=0.753, rely=0.109, height=33, width=49)
        self.emailButton.configure(activebackground="#d9d9d9")
        self.emailButton.configure(activeforeground="#000000")
        self.emailButton.configure(background="#d9d9d9")
        self.emailButton.configure(disabledforeground="#a3a3a3")
        self.emailButton.configure(foreground="#000000")
        self.emailButton.configure(highlightbackground="#d9d9d9")
        self.emailButton.configure(highlightcolor="black")
        self.emailButton.configure(pady="0")
        self.emailButton.configure(command=lambda: controller.email(self),text='''Email''')

        self.AButton3 = tk.Button(self.Frame1)
        self.AButton3.place(relx=0.118, rely=0.436, height=33, width=89)
        self.AButton3.configure(activebackground="#d9d9d9")
        self.AButton3.configure(activeforeground="#000000")
        self.AButton3.configure(background="#d9d9d9")
        self.AButton3.configure(disabledforeground="#a3a3a3")
        self.AButton3.configure(foreground="#000000")
        self.AButton3.configure(highlightbackground="#d9d9d9")
        self.AButton3.configure(highlightcolor="black")
        self.AButton3.configure(pady="0")
        self.AButton3.configure(command=lambda: controller.assigment(self),text='''Assignment''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=26, width=142)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Report''')
        self.Label1.configure(width=142)

        self.back1 = tk.Button(top)
        self.back1.place(relx=0.014, rely=0.015, height=33, width=43)
        self.back1.configure(activebackground="#d9d9d9")
        self.back1.configure(activeforeground="#000000")
        self.back1.configure(background="#d9d9d9")
        self.back1.configure(disabledforeground="#a3a3a3")
        self.back1.configure(foreground="#000000")
        self.back1.configure(highlightbackground="#d9d9d9")
        self.back1.configure(highlightcolor="black")
        self.back1.configure(pady="0")
        self.back1.configure(command=lambda: controller.show_frame("Main"),text='''Back''')


    
    
    
if __name__ == "__main__":
    app = JoinTh_c()
    app.mainloop()

