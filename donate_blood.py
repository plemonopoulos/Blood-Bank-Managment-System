import psycopg2
from tkinter import *
from functools import partial
from PIL import ImageTk,Image
from tkinter import messagebox
from array import *


def submit_donate(donor_id, bank_id, clicked):
    # Connect
    con = psycopg2.connect(database="blood_bank_system", user="postgres", password="lemon", host="localhost", port="5432")

    # Create cursor
    cur = con.cursor()

    if clicked.get() == "A(+)":
        true_group = 'a_pos'
    elif clicked.get() == "A(-)":
        true_group = 'a_neg'
    elif clicked.get() == "B(+)":
        true_group = 'b_pos'
    elif clicked.get() == "B(-)":
        true_group = 'b_neg'
    elif clicked.get() == "O(+)":
        true_group = 'o_pos'
    elif clicked.get() == "O(-)":
        true_group = 'o_neg'
    elif clicked.get() == "AB(+)":
        true_group = 'ab_pos'
    else:
        true_group = 'ab_neg'


    select_group = """SELECT %s FROM blood_bank WHERE bank_id = %s"""
    cur.execute(select_group %(true_group, bank_id.get()))
    record_id = cur.fetchall()

    print_records = ''
    temp_record = ''

    for record in record_id:
        print_records += str(record)

    for i in range(len(print_records)):
        if(print_records[i].isnumeric()):
            temp_record += print_records[i]


    int_record = int(temp_record)
    int_record = int_record + 1


    update_query = """UPDATE blood_bank SET %s = %s WHERE bank_id = %s"""
    cur.execute(update_query % (true_group, int_record, bank_id.get()))


    bank_name_query = """SELECT bank_name FROM blood_bank WHERE bank_id = %s"""
    cur.execute(bank_name_query %(bank_id.get()))
    b_names= cur.fetchone()
    print_b_name = ''
    for b_name in b_names:
        print_b_name += str(b_name)



    donor_name_query = """SELECT name FROM donors WHERE donor_id = %s"""
    cur.execute(donor_name_query %(donor_id.get()))
    d_names = cur.fetchone()
    print_d_name = ''
    for d_name in d_names:
        print_d_name += str(d_name)


    con.commit()

    con.close()


    donor_id.delete(0, END)
    bank_id.delete(0, END)

    messagebox.showinfo("Thanks for donation !!!", "Congratulations!!!\n%s donated blood '%s' to %s" %(print_d_name, clicked.get(), print_b_name))
