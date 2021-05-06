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

    update_query = """UPDATE blood_bank SET bank_id = %s, address_id = %s, bank_name = '%s', a_pos = %s, a_neg = %s, b_pos = %s, b_neg = %s, o_pos = %s, o_neg = %s, ab_pos = %s, ab_neg = %s WHERE bank_id = %s"""
    cur.execute(update_query %(bank_id_editor.get(), address_id_editor.get(), bank_name_editor.get(), a_pos_editor.get(), a_neg_editor.get(), b_pos_editor.get(), b_neg_editor.get(), o_pos_editor.get(), o_neg_editor.get(), ab_pos_editor.get(), ab_neg_editor.get() , delete_box.get()))


    con.commit()

    con.close()

    editor.destroy()


#Create Function for edit
def edit_bank(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    global editor

    editor = Tk()
    editor.title('Update a Record for Blood Bank')
    editor.geometry("400x400")

    # Query database
    cur.execute("SELECT * FROM blood_bank WHERE bank_id = %s" %(delete_box.get()))
    records = cur.fetchall()

    #Create global variables
    global bank_id_editor
    global address_id_editor
    global bank_name_editor
    global a_pos_editor
    global a_neg_editor
    global b_pos_editor
    global b_neg_editor
    global o_pos_editor
    global o_neg_editor
    global ab_pos_editor
    global ab_neg_editor

    # Create Text Boxes
    bank_id_editor = Entry(editor, width=30)
    bank_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    address_id_editor = Entry(editor, width=30)
    address_id_editor.grid(row=1, column=1, padx=20)
    bank_name_editor = Entry(editor, width=30)
    bank_name_editor.grid(row=2, column=1, padx=20)
    a_pos_editor = Entry(editor, width=30)
    a_pos_editor.grid(row=3, column=1, padx=20)
    a_neg_editor = Entry(editor, width=30)
    a_neg_editor.grid(row=4, column=1, padx=20)
    b_pos_editor = Entry(editor, width=30)
    b_pos_editor.grid(row=5, column=1, padx=20)
    b_neg_editor = Entry(editor, width=30)
    b_neg_editor.grid(row=6, column=1, padx=20)
    o_pos_editor = Entry(editor, width=30)
    o_pos_editor.grid(row=7, column=1, padx=20)
    o_neg_editor = Entry(editor, width=30)
    o_neg_editor.grid(row=8, column=1, padx=20)
    ab_pos_editor = Entry(editor, width=30)
    ab_pos_editor.grid(row=9, column=1, padx=20)
    ab_neg_editor = Entry(editor, width=30)
    ab_neg_editor.grid(row=10, column=1, padx=20)

    # Create Text Box Labels
    bank_id_label_editor = Label(editor, text="Bank_id")
    bank_id_label_editor.grid(row=0, column=0, pady=(10, 0))
    address_id_label_editor = Label(editor, text="Address_id")
    address_id_label_editor.grid(row=1, column=0)
    bank_name_label_editor = Label(editor, text="Bank_name")
    bank_name_label_editor.grid(row=2, column=0)
    a_pos_label_editor = Label(editor, text="A(+)")
    a_pos_label_editor.grid(row=3, column=0)
    a_neg_label_editor = Label(editor, text="A(-)")
    a_neg_label_editor.grid(row=4, column=0)
    b_pos_label_editor = Label(editor, text="B(+)")
    b_pos_label_editor.grid(row=5, column=0)
    b_neg_label_editor = Label(editor, text="B(-)")
    b_neg_label_editor.grid(row=6, column=0)
    o_pos_label_editor = Label(editor, text="O(+)")
    o_pos_label_editor.grid(row=7, column=0)
    o_neg_label_editor = Label(editor, text="O(-)")
    o_neg_label_editor.grid(row=8, column=0)
    ab_pos_label_editor = Label(editor, text="AB(+)")
    ab_pos_label_editor.grid(row=9, column=0)
    ab_neg_label_editor = Label(editor, text="AB(-)")
    ab_neg_label_editor.grid(row=10, column=0)


    # Loop thru results
    for record in records:
        bank_id_editor.insert(0, record[0])
        address_id_editor.insert(0, record[1])
        bank_name_editor.insert(0, record[2])
        a_pos_editor.insert(0, record[3])
        a_neg_editor.insert(0, record[4])
        b_pos_editor.insert(0, record[5])
        b_neg_editor.insert(0, record[6])
        o_pos_editor.insert(0, record[7])
        o_neg_editor.insert(0, record[8])
        ab_pos_editor.insert(0, record[9])
        ab_neg_editor.insert(0, record[10])


    # Create Save Button
    update1 = partial(update, delete_box)
    save_btn = Button(editor, text="Save Record", command=update1, bg="royal blue", fg="white")
    save_btn.grid(row=11, column=1, columnspan=10, pady=10, padx=10, ipadx=70)


    con.commit()

    con.close()


#Create Function for delete
def delete_bank(delete_box):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    #Delete a record
    cur.execute("DELETE FROM donors WHERE bank_id = %s" % (delete_box.get()))
    cur.execute("DELETE FROM staff WHERE bank_id = %s" % (delete_box.get()))
    cur.execute("DELETE FROM contact WHERE bank_id = %s" % (delete_box.get()))
    cur.execute("DELETE FROM blood_bank WHERE bank_id = %s" %(delete_box.get()))

    delete_box.delete(0, END)

    con.commit()

    con.close()


#Create Submit Function for database
def submit_bank(bank_id, address_id, bank_name, a_pos, a_neg, b_pos, b_neg, o_pos, o_neg, ab_pos, ab_neg):
    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    #Create cursor
    cur = con.cursor()

    #Insert into table
    insert_query = """INSERT INTO blood_bank (bank_id, address_id, bank_name, a_pos, a_neg, b_pos, b_neg, o_pos, o_neg, ab_pos, ab_neg) VALUES (%s, %s, '%s', %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(insert_query %(bank_id.get(), address_id.get(), bank_name.get(), a_pos.get(), a_neg.get(), b_pos.get(), b_neg.get(), o_pos.get(), o_neg.get(), ab_pos.get(), ab_neg.get()))


    con.commit()

    con.close()

    #Clear the text boxes
    bank_id.delete(0, END)
    address_id.delete(0, END)
    bank_name.delete(0, END)
    a_pos.delete(0, END)
    a_neg.delete(0, END)
    b_pos.delete(0, END)
    b_neg.delete(0, END)
    o_pos.delete(0, END)
    o_neg.delete(0, END)
    ab_pos.delete(0, END)
    ab_neg.delete(0, END)

def query_bank():

    #Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")
    # Create cursor
    cur = con.cursor()

    top = Toplevel()
    top.title('Blood Bank info')


    #Query database
    cur.execute("SELECT * FROM blood_bank")
    records = cur.fetchall()

    #Loop thru results

    print_records = ''

    for record in records:
        for i in range(11):
            print_records += str(record[i]) + "\t"
        print_records += "\n"


    query_label = Label(top, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)


    con.commit()

    con.close()