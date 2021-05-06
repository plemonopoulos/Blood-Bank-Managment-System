import psycopg2
from tkinter import *
from functools import partial
from PIL import ImageTk,Image
from tkinter import messagebox
from array import *


#Create Function for udate
def update(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    update_query = """UPDATE staff SET staff_id = %s, bank_id = %s, staff_name = '%s', job_title = '%s', phone = '%s', salary = %s WHERE staff_id = %s"""
    cur.execute(update_query %(staff_id_editor.get(), bank_id_editor.get(), staff_name_editor.get(), job_title_editor.get(), phone_editor.get(), salary_editor.get(), delete_box.get()))


    con.commit()

    con.close()

    editor.destroy()

#Create Function for edit
def edit_staff(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    global editor

    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x300")

    # Query database
    cur.execute("SELECT * FROM staff WHERE staff_id = %s" %(delete_box.get()))
    records = cur.fetchall()

    #Create global variables
    global staff_id_editor
    global bank_id_editor
    global staff_name_editor
    global job_title_editor
    global phone_editor
    global salary_editor

    # Create Text Boxes
    staff_id_editor = Entry(editor, width=30)
    staff_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    bank_id_editor = Entry(editor, width=30)
    bank_id_editor.grid(row=1, column=1, padx=20)
    staff_name_editor = Entry(editor, width=30)
    staff_name_editor.grid(row=2, column=1, padx=20)
    job_title_editor = Entry(editor, width=30)
    job_title_editor.grid(row=3, column=1, padx=20)
    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=4, column=1, padx=20)
    salary_editor = Entry(editor, width=30)
    salary_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    staff_id_label_editor = Label(editor, text="Staff_id")
    staff_id_label_editor.grid(row=0, column=0, pady=(10, 0))
    bank_id_label_editor = Label(editor, text="Bank_id")
    bank_id_label_editor.grid(row=1, column=0)
    staff_name_label_editor = Label(editor, text="Staff_name")
    staff_name_label_editor.grid(row=2, column=0)
    job_title_label_editor = Label(editor, text="Job_title")
    job_title_label_editor.grid(row=3, column=0)
    phone_label_editor = Label(editor, text="Phone")
    phone_label_editor.grid(row=4, column=0)
    salary_label_editor = Label(editor, text="Salary")
    salary_label_editor.grid(row=5, column=0)


    # Loop thru results
    for record in records:
        staff_id_editor.insert(0, record[0])
        bank_id_editor.insert(0, record[1])
        staff_name_editor.insert(0, record[2])
        job_title_editor.insert(0, record[3])
        phone_editor.insert(0, record[4])
        salary_editor.insert(0, record[5])


    # Create Save Button
    update1 = partial(update, delete_box)
    save_btn = Button(editor, text="Save Record", command=update1, bg="royal blue", fg="white")
    save_btn.grid(row=6, column=1, columnspan=10, pady=10, padx=10, ipadx=70)


    con.commit()

    con.close()


#Create Function for delete
def delete_staff(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    #Delete a record
    cur.execute("DELETE FROM staff WHERE staff_id = %s" %(delete_box.get()))

    delete_box.delete(0, END)

    con.commit()

    con.close()


#Create Submit Function for database
def submit_staff(staff_id, bank_id, staff_name, job_title, phone, salary):
    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    #Create cursor
    cur = con.cursor()

    #Insert into table
    insert_query = """INSERT INTO staff (staff_id, bank_id, staff_name, job_title, phone, salary) VALUES (%s, %s, '%s', '%s', '%s', %s)"""
    #record_to_insert = (donor_id.get())
    cur.execute(insert_query %(staff_id.get(), bank_id.get(), staff_name.get(), job_title.get(), phone.get(), salary.get()))


    con.commit()

    con.close()

    #Clear the text boxes
    staff_id.delete(0, END)
    bank_id.delete(0, END)
    staff_name.delete(0, END)
    job_title.delete(0, END)
    phone.delete(0, END)
    salary.delete(0, END)

def query_staff():

    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")
    # Create cursor
    cur = con.cursor()

    top = Toplevel()
    top.title('All employers')


    #Query database
    cur.execute("SELECT * FROM staff")
    records = cur.fetchall()

    #Loop thru results

    print_records = ''

    for record in records:
        for i in range(6):
            print_records += str(record[i]) + "\t"
        print_records += "\n"


    query_label = Label(top, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)


    con.commit()

    con.close()

