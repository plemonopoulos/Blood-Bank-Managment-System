from tkinter import *
from functools import partial
import psycopg2
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from array import *
from donors_gui import *
from blood_bank import *
from staff import *
from donate_blood import *


#Create & Configure root
menu = Tk()
Grid.rowconfigure(menu, 0, weight=1)
Grid.columnconfigure(menu, 0, weight=1)

con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")
cur = con.cursor()

print("Database opened successfully")

#Create & Configure frame
frame=Frame(menu)
frame.grid(row=0, column=0, sticky=N+S+E+W)
Grid.rowconfigure(frame, 0, weight=1)
Grid.rowconfigure(frame, 1, weight=1)
Grid.rowconfigure(frame, 2, weight=1)
Grid.rowconfigure(frame, 3, weight=1)
Grid.rowconfigure(frame, 4, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

root=Frame(menu)
root.grid(row=0, column=0, sticky=N+S+E+W)

bank=Frame(menu)
bank.grid(row=0, column=0, sticky=N+S+E+W)

staff=Frame(menu)
staff.grid(row=0, column=0, sticky=N+S+E+W)

donate=Frame(menu)
donate.grid(row=0, column=0, sticky=N+S+E+W)

################
#Create Text Boxes
donor_id = Entry(root, width=30)
donor_id.grid(row=0, column=1, padx=20, pady=(10, 0))
bank_id = Entry(root, width=30)
bank_id.grid(row=1, column=1, padx=20)
address_id = Entry(root, width=30)
address_id.grid(row=2, column=1, padx=20)
name = Entry(root, width=30)
name.grid(row=3, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=4, column=1, padx=20)
sex = Entry(root, width=30)
sex.grid(row=5, column=1, padx=20)
phone = Entry(root, width=30)
phone.grid(row=6, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20, pady=5)

#Create Text Box Labels
donor_id_label = Label(root, text="Donor_id")
donor_id_label.grid(row=0, column=0, pady=(10, 0))
bank_id_label = Label(root, text="Bank_id")
bank_id_label.grid(row=1, column=0)
address_id_label = Label(root, text="Address_id")
address_id_label.grid(row=2, column=0)
name_label = Label(root, text="Name")
name_label.grid(row=3, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=4, column=0)
sex_label = Label(root, text="Sex(M/F)")
sex_label.grid(row=5, column=0)
phone_label = Label(root, text="Phone")
phone_label.grid(row=6, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

#Create Submit Button
submit1 = partial(submit, donor_id, bank_id, address_id, name, age, sex, phone)
submit_btn = Button(root, text="Insert Record", command=submit1, bg="royal blue", fg="white")
submit_btn.grid(row=7, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create query button
query_btn = Button(root, text="Show Records", command=query, bg="royal blue", fg="white")
query_btn.grid(row=8, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create delete button
delete1 = partial(delete, delete_box)
delete_btn = Button(root, text="Delete Record", command=delete1, bg="royal blue", fg="white")
delete_btn.grid(row=10, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create udate button
edit1 = partial(edit, delete_box)
edit_btn = Button(root, text="Update Record", command=edit1, bg="royal blue", fg="white")
edit_btn.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create back button

back= Button(root, text="Back",command=frame.tkraise, bg="tomato", fg="white")
back.grid(row=11,column=10,padx=200, pady=50, sticky=N+S+E+W)

########################
#Blood Bank
########################

#Create Text Boxes
bank_id = Entry(bank, width=30)
bank_id.grid(row=0, column=1, padx=20, pady=(10, 0))
address_id = Entry(bank, width=30)
address_id.grid(row=1, column=1, padx=20)
bank_name = Entry(bank, width=30)
bank_name.grid(row=2, column=1, padx=20)
a_pos = Entry(bank, width=30)
a_pos.grid(row=3, column=1, padx=20)
a_neg = Entry(bank, width=30)
a_neg.grid(row=4, column=1, padx=20)
b_pos = Entry(bank, width=30)
b_pos.grid(row=5, column=1, padx=20)
b_neg = Entry(bank, width=30)
b_neg.grid(row=6, column=1, padx=20)
o_pos = Entry(bank, width=30)
o_pos.grid(row=7, column=1, padx=20)
o_neg = Entry(bank, width=30)
o_neg.grid(row=8, column=1, padx=20)
ab_pos = Entry(bank, width=30)
ab_pos.grid(row=9, column=1, padx=20)
ab_neg = Entry(bank, width=30)
ab_neg.grid(row=10, column=1, padx=20)
delete_box = Entry(bank, width=30)
delete_box.grid(row=13, column=1, padx=20, pady=5)


#Create Text Box Labels
bank_id_label = Label(bank, text="Bank_id")
bank_id_label.grid(row=0, column=0, pady=(10, 0))
address_id_label = Label(bank, text="Address_id")
address_id_label.grid(row=1, column=0)
bank_name_label = Label(bank, text="Bank_name")
bank_name_label.grid(row=2, column=0)
a_pos_label = Label(bank, text="A(+)")
a_pos_label.grid(row=3, column=0)
a_neg_label = Label(bank, text="A(-)")
a_neg_label.grid(row=4, column=0)
b_pos_label = Label(bank, text="B(+)")
b_pos_label.grid(row=5, column=0)
b_neg_label = Label(bank, text="B(-)")
b_neg_label.grid(row=6, column=0)
o_pos_label = Label(bank, text="O(+)")
o_pos_label.grid(row=7, column=0)
o_neg_label = Label(bank, text="O(-)")
o_neg_label.grid(row=8, column=0)
ab_pos_label = Label(bank, text="AB(+)")
ab_pos_label.grid(row=9, column=0)
ab_neg_label = Label(bank, text="AB(-)")
ab_neg_label.grid(row=10, column=0)
delete_box_label = Label(bank, text="Select ID")
delete_box_label.grid(row=13, column=0, pady=5)

#Create Submit Button
submit_bank1 = partial(submit_bank, bank_id, address_id, bank_name, a_pos, a_neg, b_pos, b_neg, o_pos, o_neg, ab_pos, ab_neg)
submit_btn = Button(bank, text="Insert Record", command=submit_bank1, bg="royal blue", fg="white")
submit_btn.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create query button
query_btn = Button(bank, text="Show Records", command=query_bank, bg="royal blue", fg="white")
query_btn.grid(row=12, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create delete button
delete_bank1 = partial(delete_bank, delete_box)
delete_btn = Button(bank, text="Delete Record", command=delete_bank1, bg="royal blue", fg="white")
delete_btn.grid(row=14, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create udate button
edit_bank1 = partial(edit_bank, delete_box)
edit_btn = Button(bank, text="Update Record", command=edit_bank1, bg="royal blue", fg="white")
edit_btn.grid(row=15, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create back button

back= Button(bank, text="Back",command=frame.tkraise, bg="tomato", fg="white")
back.grid(row=15,column=10,padx=200, pady=10, sticky=N+S+E+W)

############################
# Staff
####################################

#Create Text Boxes
staff_id = Entry(staff, width=30)
staff_id.grid(row=0, column=1, padx=20, pady=(10, 0))
bank_id = Entry(staff, width=30)
bank_id.grid(row=1, column=1, padx=20)
staff_name = Entry(staff, width=30)
staff_name.grid(row=2, column=1, padx=20)
job_title = Entry(staff, width=30)
job_title.grid(row=3, column=1, padx=20)
phone = Entry(staff, width=30)
phone.grid(row=4, column=1, padx=20)
salary = Entry(staff, width=30)
salary.grid(row=5, column=1, padx=20)

delete_box = Entry(staff, width=30)
delete_box.grid(row=8, column=1, padx=20, pady=5)

#Create Text Box Labels
staff_id_label = Label(staff, text="Staff_id")
staff_id_label.grid(row=0, column=0, pady=(10, 0))
bank_id_label = Label(staff, text="Bank_id")
bank_id_label.grid(row=1, column=0)
staff_name_label = Label(staff, text="Staff_name")
staff_name_label.grid(row=2, column=0)
job_title_label = Label(staff, text="Job_title")
job_title_label.grid(row=3, column=0)
phone_label = Label(staff, text="Phone")
phone_label.grid(row=4, column=0)
salary_label = Label(staff, text="Salary")
salary_label.grid(row=5, column=0)

delete_box_label = Label(staff, text="Select ID")
delete_box_label.grid(row=8, column=0, pady=5)

#Create Submit Button
submit_staff1 = partial(submit_staff, staff_id, bank_id, staff_name, job_title, phone, salary)
submit_btn = Button(staff, text="Insert Record", command=submit_staff1, bg="royal blue", fg="white")
submit_btn.grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create query button
query_btn = Button(staff, text="Show Records", command=query_staff, bg="royal blue", fg="white")
query_btn.grid(row=7, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create delete button
delete_staff1 = partial(delete_staff, delete_box)
delete_btn = Button(staff, text="Delete Record", command=delete_staff1, bg="royal blue", fg="white")
delete_btn.grid(row=9, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create udate button
edit_staff1 = partial(edit_staff, delete_box)
edit_btn = Button(staff, text="Update Record", command=edit_staff1, bg="royal blue", fg="white")
edit_btn.grid(row=10, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create back button

back= Button(staff, text="Back",command=frame.tkraise, bg="tomato", fg="white")
back.grid(row=15,column=10,padx=200, pady=10, sticky=N+S+E+W)

#####################################
#Donate Blood
#######################################

#Create Text Boxes
donor_id = Entry(donate, width=30)
donor_id.grid(row=0, column=1, padx=20, pady=(10, 0))
bank_id = Entry(donate, width=30)
bank_id.grid(row=1, column=1, padx=20)
#blood_group = Entry(donate, width=30)
#blood_group.grid(row=2, column=1, padx=20)

clicked = StringVar()
clicked.set("A(+)")

blood_group = OptionMenu(donate, clicked, "A(+)", "A(-)", "B(+)", "B(-)", "O(+)", "O(-)", "AB(+)", "AB(-)")
blood_group.grid(row=2, column=1, padx=20)

#Create Text Box Labels
donor_id_label = Label(donate, text="Donor_id")
donor_id_label.grid(row=0, column=0)
bank_id_label = Label(donate, text="Bank_id")
bank_id_label.grid(row=1, column=0)
blood_group_label = Label(donate, text="Blood_group")
blood_group_label.grid(row=2, column=0)


#Create Submit Button
submit_donate1 = partial(submit_donate, donor_id, bank_id, clicked)
submit_btn = Button(donate, text="Save Donation", command=submit_donate1, bg="royal blue", fg="white", font=("bold"))
submit_btn.grid(row=3, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

#Create back button
back= Button(donate, text="Back",command=frame.tkraise, bg="tomato", fg="white")
back.grid(row=3,column=10,padx=200, pady=10, sticky=N+S+E+W)



#######################################

frame3=Frame(menu)
frame3.grid(row=0, column=0, sticky=N+S+E+W)
frame4=Frame(menu)
frame4.grid(row=0, column=0, sticky=N+S+E+W)




img = PhotoImage(file="img.png")
img = img.subsample(1, 1)


background = Label(frame, image=img, bd=0)
background.place(x=0, y=0, relwidth=1, relheight=1)
background.image = img

lbl=Label(frame,text="Blood Bank Managment",bg="cyan",fg="red",font=  ("Times","25","bold italic"))
lbl.grid(row=0,column=0)

btn1 = Button(frame, text="Donor Entry",command=root.tkraise, bg="tomato", fg="white", font=("bold"))
btn1.grid(row=1,column=0,padx=200, pady=20, sticky=N+S+E+W)


btn2 = Button(frame, text="Bank Entry",command=bank.tkraise, bg="tomato", fg="white", font=("bold"))
btn2.grid(row=2,column=0,padx=200, pady=20, sticky=N+S+E+W)


btn3 = Button(frame, text="Staff Entry",command=staff.tkraise, bg="tomato", fg="white", font=("bold"))
btn3.grid(row=3,column=0,padx=200, pady=20, sticky=N+S+E+W)

btn4 = Button(frame, text="Donate Blood",command=donate.tkraise, bg="tomato", fg="white", font=("bold"))
btn4.grid(row=4,column=0,padx=200, pady=20, sticky=N+S+E+W)



quitbutton = Button(frame, text="Exit",command=menu.destroy, bg="tomato", fg="white", font=("bold"))
quitbutton.grid(row=5,column=0,padx=200, pady=20, sticky=N+S+E+W)



back= Button(frame4, text="Back",command=frame.tkraise)
back.grid(row=3,column=0,padx=50, pady=50, sticky=N+S+E+W)



frame.tkraise()
menu.geometry("600x480")
menu.title("Blood Bank Managment System")

print("\n")

#Commit changes
con.commit()

print("Operation done successfully")
con.close()

menu.mainloop()
