from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
from tkinter.ttk import Style
from tkinter.font import Font
from tkinter import Image
import sqlite3
con=sqlite3.connect('pharamcy.db')
cur=con.cursor()

root=Tk()
width=1100
height=600 
fg='#009696'
bg='black'
text=('tahoma',24)
x=100
y=100
root.geometry(f"{width}x{height}+{x}+{y}")
root.title("Valencia")
root.resizable('false','false')

def destroy():
    for frame in main_frame1.winfo_children():
        frame.destroy()


def show(page):
    
    destroy()
    page()


#main_frame
main_frame1=Frame(root,highlightbackground='black',highlightthickness=2,bg='#009696')
main_frame1.configure(width=1100,height=600)
main_frame1.pack_propagate('false')
main_frame1.pack(side='right')





def sign_up():
    
    
   
    def add_new():
        
        messagebox.showinfo('done',"The new administrator added successfully")
    
    frame_2=Frame(main_frame1,bg=fg)
    frame_2.place(anchor='center',relx=.5,rely=.5)
    name_label=Label(frame_2,text='username',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_name=Entry(frame_2)
    password_label=Label(frame_2,text='password',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_password=Entry(frame_2,show='*')
    con_password=Label(frame_2,text='confirm password',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_cpass=Entry(frame_2,show='*')
    address_label=Label(frame_2,text='address',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_address=Entry(frame_2)
    email_label=Label(frame_2,text='email',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_email=Entry(frame_2)
    phone_label=Label(frame_2,text='phone',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_phone=Entry(frame_2)
    
    
    #test_frame to add imge #
    frame_img_s=Frame(main_frame1,bg=fg)
    frame_img_s.pack_propagate('false')
    frame_img_s.configure(width=140,height=140)
    frame_img_s.pack(side=LEFT,pady=(430,0))
    
    photo_log_s=PhotoImage(file='image/left (1).png')
    btn=Button(frame_img_s,image=photo_log_s,relief='flat',bg=fg,command=lambda:show(welcome))
    btn.pack(pady=(80,0))
    btn.photo_log_s=photo_log_s
    
    ####################################
    
  
    
    
    name_label.grid(row=0,column=0)
    txt_name.grid(row=0,column=1,padx=10,pady=10)
    email_label.grid(row=1,column=0)
    txt_email.grid(row=1,column=1,padx=10,pady=10)
    password_label.grid(row=2,column=0)
    txt_password.grid(row=2,column=1,padx=10,pady=10)
    con_password.grid(row=3,column=0)
    txt_cpass.grid(row=3,column=1,padx=10,pady=10)
    phone_label.grid(row=4,column=0) 
    txt_phone.grid(row=4,column=1,padx=10,pady=10)
    address_label.grid(row=5,column=0)
    txt_address.grid(row=5,column=1)
   
    
                # database of signup intrface #
    ###########################################################################
    def add_new_admin():
        if txt_name.get() and txt_email.get() and txt_password.get() and txt_phone.get() and txt_address.get() and len(txt_phone.get())==11 and txt_cpass.get() ==txt_password.get()  :
            con=sqlite3.connect('pharamcy.db')
            cur=con.cursor()
            username_lb=txt_name.get()
            email_lb=txt_email.get()
            password_lb=txt_password.get()
            phone_lb=txt_phone.get()
            address_lb=txt_address.get()
            cur.execute('insert into admin (username,email,password,phone,address) VALUES(?,?,?,?,?)',[username_lb,email_lb,password_lb,phone_lb,address_lb])
            con.commit()
            con.close()
            messagebox.showinfo("Done","operation accomplished successfully")
        else:
            messagebox.showwarning("warning","All data must be filled in")
    ###########################################################################
    
    rb=Button(frame_2,text='submit',font=('Tahoma',20,'bold'),bg='white',fg=bg,command=add_new_admin)
    rb.grid(row=6,column=0,columnspan=2)
   
    
def login_e ():
   
    frame_1=Frame(main_frame1,bg=fg)
    frame_1.pack_propagate('false')
    frame_1.configure(width=1100,height=600)
    frame_1.place(anchor='center',relx=.5,rely=.5)
    
    #test_frame to add imge #**********************#
    frame_img=Frame(main_frame1,bg=fg)
    frame_img.pack_propagate('false')
    frame_img.configure(width=140,height=140)
    frame_img.pack(side=TOP,pady=70)
    
    photo_log=PhotoImage(file='image/login.png')
    btn=Button(frame_img,image=photo_log,relief='flat',bg=fg)
    btn.pack()
    btn.photo_log=photo_log
    
    ####################################
    
    
    name_label=Label(frame_1,text='username',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_user=Entry(frame_1)
    password_label=Label(frame_1,text='password',font=text,padx=10,pady=10,bg=fg,fg='white')
    txt_pass=Entry(frame_1,show='*')
    rb1=Button(frame_1,text='log in',command=lambda:show(optoins),font=('Tahoma',20,'bold'),bg='white',fg=bg)
    rb2=Button(frame_1,text='sign up',command=lambda:show(sign_up),font=('Tahoma',20,'bold'),bg='white',fg=bg)
    
    
    name_label.grid(row=1,column=0)
    txt_user.grid(row=1,column=1,padx=10,pady=10)
    password_label.grid(row=2,column=0)
    txt_pass.grid(row=2,column=1,padx=10,pady=10)
    rb2.grid(row=3,column=1)
    
        # database to check username and password #
    ###########################################################################
    def checK_login():
        username_lab=txt_user.get()
        passwordlab=txt_pass.get()
        con=sqlite3.connect('pharamcy.db')
        cur=con.cursor()
        cur.execute('SELECT username,password from admin where username = ? AND password=?',[username_lab,passwordlab])
        res_log = []
        res_log=cur.fetchall()
        if not res_log :
            messagebox.showerror("error","username or password is not correct")
        else:
            show(optoins)
            
    rb1=Button(frame_1,text='log in',command=checK_login,font=('Tahoma',20,'bold'),bg='white',fg=bg)
    rb1.grid(row=3,column=0)
    ###########################################################################    

def welcome():
    frame=Frame(main_frame1,bg=fg)
    frame.configure(width=1100,height=600)
    frame.pack_propagate('false')
    frame.place(anchor='center',relx=.5,rely=.5)
    root['bg']=fg
    
    font_log1=Font(family='Helvetica',
                  size=80,
                  slant='italic',
                  weight='bold'
    )
    font_log2=Font(family='Helvetica',
                  size=42,
                  slant='roman',
                  weight='bold'
    )
    
    
    label=Label(frame,text='valencia',font=font_log1,padx=5,pady=5,fg='white',bg=fg)
    label.place(y=150,x=500)
    label2=Label(frame,text='pharmacy',font=font_log2,padx=5,pady=5,fg='white',bg=fg)
    label2.place(y=260,x=680)
    rb=Button(frame,text='continue',command=lambda:show(login_e),font=('Tahoma',20,'bold'),bg='white',fg=bg)
    rb.place(x=930,y=520)
    
    frame_img4=Frame(frame,bg=fg)
    frame_img4.pack_propagate('false')
    frame_img4.configure(width=500,height=500)
    frame_img4.pack(side=LEFT)
    
    photo_log2=PhotoImage(file='image/Premium Vector _ Pharmacist.png')
    btn_img=Button(frame_img4,image=photo_log2,relief='flat')
    btn_img.pack(side=LEFT,pady=(50,0),padx=10)
    btn_img.photo_log2=photo_log2
    
welcome()
###################################################################################


def optoins():
    def hide():
        lbl1.config(bg='#009696')
        lbl2.config(bg='#009696')
        lbl3.config(bg='#009696')
        lbl4.config(bg='#009696')
        
    # def destroy_left():
    #      fram1.destroy()
        
    def destroy():
        for frame in main_frame.winfo_children():
            frame.destroy()
            
            
            def destroy1():
                for frame in main_frame1.winfo_children():
                    frame.destroy()
            
    
    def show(lbl,page):
        hide()
        lbl.configure(bg='black')
        destroy()
        page()
    
    

        
    #left_frame
    fram1=Frame(main_frame1,bg='#009696')
    fram1.configure(width=300,height=600)
    fram1.pack_propagate('false')
    fram1.pack(side='left')
    
   
    
    
    #main_frame
    main_frame=Frame(main_frame1,highlightbackground='black',highlightthickness=2,bg='#aaa')
    main_frame.configure(width=800,height=600)
    main_frame.pack_propagate('false')
    main_frame.pack(side='right')
    
    
    # first interface to add new doctor      " صلي علي محمد"
    def modify_staff():
        #add_frame
        fram_add=Frame(main_frame,bg='#aaa')
        fram_add.configure(width=1000,height=250)
        fram_add.pack(anchor='nw',padx=70,pady=10)
        
        
        #modify the staff
        gender=['male','female']
        gender_var=StringVar()
        gender_var.set(gender[0])
        
        
        
        lbl_n=Label(fram_add,text="Name",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_n=Entry(fram_add)
        lbl_s=Label(fram_add,text="SSN",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_s=Entry(fram_add)
        lbl_sa=Label(fram_add,text="Salary",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_sa=Entry(fram_add)
        lbl_num=Label(fram_add,text="Phone",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_num=Entry(fram_add)
        lbl_Gender=Label(fram_add,text='Gender',fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        com_gender=Combobox(fram_add,value=gender,state='readonly',textvariable=gender_var)
        com_gender.grid(row=1,column=3)
       
        
        
         
        
        lbl_n.grid(row=0,column=0,padx=20,pady=20)
        en_n.grid(row=0,column=1,padx=20,pady=20)
        lbl_s.grid(row=1,column=0,padx=20,pady=20)
        en_s.grid(row=1,column=1,padx=20,pady=20)
        lbl_sa.grid(row=2,column=0,padx=20,pady=20)
        en_sa.grid(row=2,column=1,padx=20,pady=20)
        lbl_num.grid(row=0,column=2,padx=20,pady=20)
        en_num.grid(row=0,column=3,padx=20,pady=20)
        lbl_Gender.grid(row=1,column=2)
        
        
                         # Database  of first intrfce #
        ##################################################################
        
        # button_delet #
        def delete_database_store():
            ssn=int(en_s.get())
            con=sqlite3.connect('pharamcy.db')
            cursor=con.cursor()
            cursor.execute('delete from staff where ssn = ?',(ssn,))
            con.commit()
            con.close()
            messagebox.showinfo("Done","operation accomplished successfully")
        btn_delete2=Button(fram_add,text='Delete',fg='black',bg='#009696',font=('Tahoma',12,'bold'),command=delete_database_store)
        btn_delete2.grid(row=2,column=3)
        
        
        
        
        def add_datatbase():
           
                ssn_db=(en_s.get())
                name_db=en_n.get()
                phone_db=en_num.get()
                gender_db=com_gender.get()
                salary_db=(en_sa.get())
                if en_s.get() and en_n.get() and  en_num.get() and com_gender.get() and en_sa.get() and len(en_num.get())==11 and len(en_s.get())==14:
                    try:
                        ssn_db=int(en_s.get())
                        name_db=en_n.get()
                        phone_db=en_num.get()
                        gender_db=com_gender.get()
                        salary_db=int(en_sa.get())
                        con=sqlite3.connect('pharamcy.db')
                        cur=con.cursor()
                        cur.execute('INSERT INTO staff(ssn,name,phone, gender,salary) VALUES(?,?,?,?,?)',[ssn_db,name_db,phone_db,gender_db,salary_db])
                        con.commit()
                        con.close()
                        messagebox.showinfo("Done","operation accomplished successfully")
                    except:
                        messagebox.showinfo("n","error")
                else:
                    messagebox.showwarning("warning","All data must be filled in")
                
        def show_database():
            for item in table1.get_children():
                          table1.delete(item)
            con=sqlite3.connect('pharamcy.db')
            cur=con.cursor()
            cur.execute('select * from staff')
            res=cur.fetchall()
            for res1 in res:
                #table1.delete()
                table1.insert('', 'end',iid=res1[0], values=res1)
            
            con.close()
        ####################################################################
        
        
        #table_fram
        fram_table=Frame(main_frame,bg='#009696')
        fram_table.configure(width=800,height=250)
        fram_table.pack(anchor='s',padx=20,pady=20)
        
        
        
        
        colums1=['ssn','name','phone','Gender','salary']
        table1=Treeview(fram_table,columns=colums1,show='headings',height=7,selectmode='browse')
        btn_show_staff=Button(fram_table,text='refresh',bg='#009696',fg='black',font=('Arial',12,'bold'),command=show_database)
        table1.column('ssn',width=130,anchor='center')
        table1.column('name',width=130,anchor='center')
        table1.column('phone',width=130,anchor='center')
        table1.column('Gender',width=130,anchor='center')
        table1.column('salary',width=130,anchor='center')
        table1.heading('ssn', text='ssn')
        table1.heading('name', text='name')
        table1.heading('phone', text='phone')
        table1.heading('Gender', text='Gender')
        table1.heading('salary', text='salary')
        table1.grid(row=0,column=0,padx=30,pady=30)
        
        scrool1=Scrollbar(fram_table,orient='vertical',command=table1.yview,bg='black')
        table1.configure(yscroll=scrool1.set)
        scrool1.grid(row=0,column=1,sticky='sn',rowspan=2)
        btn_show_staff.grid(row=1,column=0)
        
        
        style1=Style()
        style1.configure(style1, font=('Tahoma',50,'bold'))
        
        
        btn_add_staff=Button(fram_add,text='ADD',fg='black',bg='#009696',font=('Tahoma',12,'bold'),command=add_datatbase)
        btn_add_staff.grid(row=2,column=2)
    
        
    
    #secound interface to modify in the store  
       
    def modify_store():
        #add_frame
        fram_add=Frame(main_frame,bg='#aaa')
        fram_add.configure(width=800,height=250)
        fram_add.pack(anchor='nw',padx=70,pady=30)
        # database of secound interface #
    ##########################################################################
        
        # button_delet #
        def delete_database_store():
            name=en_n.get()
            con=sqlite3.connect('pharamcy.db')
            cursor=con.cursor()
            cursor.execute('delete from store where drugname = ?',(name,))
            con.commit()
            con.close()
            messagebox.showinfo("Done","operation accomplished successfully")
        btn_delete2=Button(fram_add,text='Delete',fg='black',bg='#009696',font=('Tahoma',12,'bold'),command=delete_database_store)
        btn_delete2.grid(row=1,column=3)
        
        # button_add #
        def add_database_store():
            if en_n.get() and en_q.get() and en_price.get():
                name=en_n.get()
                quan=int(en_q.get())
                price=int(en_price.get())
                con=sqlite3.connect('pharamcy.db')
                cursor=con.cursor()
                cursor.execute('insert into store values (?,?,?)',(name,quan,price))
                con.commit()
                con.close()
                messagebox.showinfo("Done","operation accomplished successfully")
            else:
               messagebox.showwarning("warning","All data must be filled in") 
            # show_in_table #
        def show_store():
            for item in table1.get_children():
                          table1.delete(item)
            con=sqlite3.connect('pharamcy.db')
            cursor=con.cursor()
            cursor.execute('SELECT drugname ,quantity FROM store')
            results = cursor.fetchall()
            for res in results:
                table1.insert('','end',values=res)
            con.close()

###############################################################################
    
    
    
        #modify the staff
        lbl_n=Label(fram_add,text="Drug name",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_n=Entry(fram_add)
        lbl_q=Label(fram_add,text="Quantity",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_q=Entry(fram_add)
        lbl_price=Label(fram_add,text="Price",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_price=Entry(fram_add)
        btn_add2=Button(fram_add,text='ADD',fg='black',bg='#009696',font=('Tahoma',12,'bold'),command=add_database_store)
    
    
    
        lbl_n.grid(row=0,column=0,padx=20,pady=20)
        en_n.grid(row=0,column=1,padx=20,pady=20)
        lbl_q.grid(row=0,column=2,padx=10,pady=10)
        en_q.grid(row=0,column=3,padx=25,pady=25)
        lbl_price.grid(row=1,column=0)
        en_price.grid(row=1,column=1)
        btn_add2.grid(row=1,column=2)
    
    
    
    
        #table_fram
        fram_table=Frame(main_frame,bg='#009696')
        fram_table.configure(width=800,height=250)
        fram_table.pack(anchor='s',padx=20,pady=20)
    
    
    
    
        colums1=['Drug name','Quantity']
        table1=Treeview(fram_table,columns=colums1,show='headings',height=10,selectmode='browse')
        btn_delet_staff2=Button(fram_table,text='refresh',bg='#009696',fg='black',font=('Arial',12,'bold'),command=show_store)
        table1.column('Drug name',width=130,anchor='center')
        table1.column('Quantity',width=130,anchor='center')
        table1.heading('Drug name', text='Drug name')
        table1.heading('Quantity', text='Quantity')
        table1.grid(row=0,column=0,padx=30,pady=30)
        scrool1=Scrollbar(fram_table,orient='vertical',command=table1.yview,bg='black')
        table1.configure(yscroll=scrool1.set)
        scrool1.grid(row=0,column=1,sticky='sn',rowspan=2)
        btn_delet_staff2.grid(row=1,column=0)
    
        style1=Style()
        style1.configure(style1, font=('Tahoma',20))
    
    #third interface using in sale
    def sales():
        #add_frame
        fram_add=Frame(main_frame,bg='#aaa')
        fram_add.configure(width=1000,height=250)
        fram_add.pack(anchor='nw',padx=70,pady=10)
        
        
        #modify the staff
        gender=['male','female']
        gender_var=StringVar()
        gender_var.set(gender[0])
        
        
        
        lbl_name=Label(fram_add,text="name",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_name=Entry(fram_add)
        lbl_phone=Label(fram_add,text="phone number",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_phone=Entry(fram_add)
        lbl_dname=Label(fram_add,text="Drug Name",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_dname=Entry(fram_add)
        lbl_quntity=Label(fram_add,text="Quantity",fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_quantity=Entry(fram_add)
        lbl_price=Label(fram_add,text='price',fg='#009696',bg='#aaa',font=('Arial',20,'bold'))
        en_price=Entry(fram_add)
        
    
        
        lbl_name.grid(row=0,column=0,padx=10,pady=10)
        en_name.grid(row=0,column=1,padx=10,pady=10)
        lbl_phone.grid(row=1,column=0,padx=10,pady=10)
        en_phone.grid(row=1,column=1,padx=10,pady=10)
        lbl_dname.grid(row=2,column=0,padx=10,pady=10)
        en_dname.grid(row=2,column=1,padx=10,pady=10)
        lbl_quntity.grid(row=0,column=2,padx=10,pady=10)
        en_quantity.grid(row=0,column=3,padx=10,pady=10)
        lbl_price.grid(row=1,column=2,padx=10,pady=10)
        en_price.grid(row=1,column=3,padx=5,pady=5)
        
        
        
            # database sales #
    ###########################################################################    
       
        
        def add_sales():
            if en_name.get() and en_dname.get() and en_quantity.get() and en_price.get():
                con=sqlite3.connect('pharamcy.db')
                cursor=con.cursor()
                namel=en_name.get()
                phonel=int(en_phone.get())
                drugnamel=en_dname.get()
                quantityl=int(en_quantity.get())
                pricel=int(en_price.get())
                cursor.execute('SELECT quantity from store WHERE drugname=?',[drugnamel])
                res8=cursor.fetchone()
                res7=int(res8[0])
                #print(res8[0])
                cursor.execute('UPDATE store set quantity =? WHERE drugname=?',[res7,drugnamel])
                cursor.execute('INSERT INTO sales(name,phone,drugname,quntity,price) VALUES (?,?,?,?,?)',[namel,phonel,drugnamel,quantityl,pricel])
                con.commit()
                con.close()
                messagebox.showinfo("Done","operation accomplished successfully")
            else:
                messagebox.showwarning("warning","All data must be filled in")
        
        btn_add_staff=Button(fram_add,text='Finish',fg='black',bg='#009696',font=('Tahoma',12,'bold'),command=(add_sales))
        btn_add_staff.grid(row=2,column=2,columnspan=2)
        
        def show_database1():
            for item in table1.get_children():
                          table1.delete(item)
            con=sqlite3.connect('pharamcy.db')
            cur=con.cursor()
            cur.execute('select name,phone,drugname,quntity,price from sales')
            res=cur.fetchall()
            for res1 in res:
                #table1.delete()
                table1.insert('', 'end', values=res1)
            
            con.close()
            
    ###########################################################################
    
    
    
    #table_fram
        fram_table=Frame(main_frame,bg='#009696')
        fram_table.configure(width=800,height=250)
        fram_table.pack(anchor='s',padx=20,pady=20)
        
        
        
        
        colums1=['Name','phone number','drug name','quantity','price']
        table1=Treeview(fram_table,columns=colums1,show='headings',height=10,selectmode='browse')
        btn_delet_staff=Button(fram_table,text='Show sales',bg='#009696',fg='black',font=('Arial',12,'bold'),command=show_database1)
        table1.column('Name',width=130,anchor='center')
        table1.column('phone number',width=130,anchor='center')
        table1.column('drug name',width=130,anchor='center')
        table1.column('quantity',width=130,anchor='center')
        table1.column('price',width=130,anchor='center')
        table1.heading('Name', text='Name')
        table1.heading('phone number', text='phone number')
        table1.heading('drug name', text='drug name')
        table1.heading('quantity', text='quantity')
        table1.heading('price', text='price')
        table1.grid(row=0,column=0,padx=30,pady=30)
        
        scrool1=Scrollbar(fram_table,orient='vertical',command=table1.yview,bg='black')
        table1.configure(yscroll=scrool1.set)
        scrool1.grid(row=0,column=1,sticky='sn',rowspan=2)
        btn_delet_staff.grid(row=1,column=0)
        
        style1=Style()
        style1.configure(style1, font=('Tahoma',20))
        
        
    def exitButton():
            clear=messagebox.askyesno('Pharmacy Management System','Confirm if you want to Exit')
            if clear>0:
                root.destroy()
            
   
        
    
    
    btn_staff=Button(fram1,text='Modify the staff',font=('Tahoma',15,'bold'),bg='#009696',relief='flat',command=lambda:show(lbl1,modify_staff))
    lbl1=Label(fram1,bg='#009696',text='')
    lbl1.place(x=50,y=70,width=5,height=40)
    
    btn_store=Button(fram1,text='Modify the store',font=('Tahoma',15,'bold'),bg='#009696',relief='flat',command=lambda:show(lbl2,modify_store))
    lbl2=Label(fram1,bg='#009696',text='')
    lbl2.place(x=50,y=120,width=5,height=40)
    
    
    btn_sales=Button(fram1,text='Sales',font=('Tahoma',15,'bold'),bg='#009696',relief='flat',command=lambda:show(lbl3,sales))
    lbl3=Label(fram1,bg='#009696',text='')
    lbl3.place(x=50,y=170,width=5,height=40)
    
    btn_exit=Button(fram1,text='Exit',font=('Tahoma',15,'bold'),bg='#009696',relief='flat',command=exitButton)
    lbl4=Label(fram1,bg='#009696',text='')
    lbl4.place(x=50,y=220,width=5,height=40)
    
    
    
    btn_staff.place(x=50,y=70)
    btn_store.place(x=50,y=120)
    btn_sales.place(x=50,y=170)
    btn_exit.place(x=50,y=220)
    
    
    
    #test_frame to add imge #**********************#
    def show1(page):    # to destroy main_fram and left frame and move to the welcome frame #
        fram1.destroy()                                                                     #
        page()                                                                              #
                                                                                            #
    
    frame_img2=Frame(fram1,bg=fg)
    frame_img2.pack_propagate('false')
    frame_img2.configure(width=400,height=140)
    frame_img2.pack(side=BOTTOM,padx=0)
    
    photo_log2=PhotoImage(file='image/left (1).png')
    btn_img=Button(frame_img2,image=photo_log2,relief='flat',bg=fg,command=lambda:show1(welcome))
    btn_img.pack(side=LEFT,pady=(50,0),padx=10)
    btn_img.photo_log2=photo_log2
    
    #####**************************************************************########################
    
    

###############################################################################################
root.mainloop()
       