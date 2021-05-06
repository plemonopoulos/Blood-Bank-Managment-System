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

    update_query = """UPDATE donors SET donor_id = %s, bank_id = %s, address_id = %s, name = '%s', age = %s, sex = '%s', phone = '%s' WHERE donor_id = %s"""
    cur.execute(update_query %(donor_id_editor.get(), bank_id_editor.get(), address_id_editor.get(), name_editor.get(), age_editor.get(), sex_editor.get(), phone_editor.get(), delete_box.get()))


    con.commit()

    con.close()

    editor.destroy()

#Create Function for edit
def edit(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    global editor

    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x600")

    # Query database
    cur.execute("SELECT * FROM donors WHERE donor_id = %s" %(delete_box.get()))
    records = cur.fetchall()

    #Create global variables
    global donor_id_editor
    global bank_id_editor
    global address_id_editor
    global name_editor
    global age_editor
    global sex_editor
    global phone_editor

    # Create Text Boxes
    donor_id_editor = Entry(editor, width=30)
    donor_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    bank_id_editor = Entry(editor, width=30)
    bank_id_editor.grid(row=1, column=1, padx=20)
    address_id_editor = Entry(editor, width=30)
    address_id_editor.grid(row=2, column=1, padx=20)
    name_editor = Entry(editor, width=30)
    name_editor.grid(row=3, column=1, padx=20)
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=4, column=1, padx=20)
    sex_editor = Entry(editor, width=30)
    sex_editor.grid(row=5, column=1, padx=20)
    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=6, column=1, padx=20)

    # Create Text Box Labels
    donor_id_label_editor = Label(editor, text="Donor_id")
    donor_id_label_editor.grid(row=0, column=0, pady=(10, 0))
    bank_id_label_editor = Label(editor, text="Bank_id")
    bank_id_label_editor.grid(row=1, column=0)
    address_id_label_editor = Label(editor, text="Address_id")
    address_id_label_editor.grid(row=2, column=0)
    name_label_editor = Label(editor, text="Name")
    name_label_editor.grid(row=3, column=0)
    age_label_editor = Label(editor, text="Age")
    age_label_editor.grid(row=4, column=0)
    sex_label_editor = Label(editor, text="Sex(M/F)")
    sex_label_editor.grid(row=5, column=0)
    phone_label_editor = Label(editor, text="Phone")
    phone_label_editor.grid(row=6, column=0)


    # Loop thru results
    for record in records:
        donor_id_editor.insert(0, record[0])
        bank_id_editor.insert(0, record[1])
        address_id_editor.insert(0, record[2])
        name_editor.insert(0, record[3])
        age_editor.insert(0, record[4])
        sex_editor.insert(0, record[5])
        phone_editor.insert(0, record[6])


    # Create Save Button
    update1 = partial(update, delete_box)
    save_btn = Button(editor, text="Save Record", command=update1, bg="royal blue", fg="white")
    save_btn.grid(row=7, column=1, columnspan=10, pady=10, padx=10, ipadx=70)


    con.commit()

    con.close()


#Create Function for delete
def delete(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    #Delete a record
    cur.execute("DELETE FROM donors WHERE donor_id = %s" %(delete_box.get()))

    delete_box.delete(0, END)

    con.commit()

    con.close()


#Create Submit Function for database
def submit(donor_id, bank_id, address_id, name, age, sex, phone):
    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    #Create cursor
    cur = con.cursor()

    #Insert into table
    insert_query = """INSERT INTO donors (donor_id, bank_id, address_id, name, age, sex, phone) VALUES (%s, %s, %s, '%s', %s, '%s', '%s')"""
    #record_to_insert = (donor_id.get())
    cur.execute(insert_query %(donor_id.get(), bank_id.get(), address_id.get(), name.get(), age.get(), sex.get(), phone.get()))


    con.commit()

    con.close()

    #Clear the text boxes
    donor_id.delete(0, END)
    bank_id.delete(0, END)
    address_id.delete(0, END)
    name.delete(0, END)
    age.delete(0, END)
    sex.delete(0, END)
    phone.delete(0, END)

def query():

    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")
    # Create cursor
    cur = con.cursor()

    top = Toplevel()
    top.title('All Donors')


    #Query database
    cur.execute("SELECT * FROM all_donors")
    #cur.execute("SELECT * FROM donors")
    records = cur.fetchall()

    #Loop thru results

    print_records = ''
    for record in records:
        for i in range(7):
            print_records += str(record[i]) + "\t\t"
        print_records += "\n"


    query_label = Label(top, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)


    con.commit()

    con.close()
